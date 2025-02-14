# MIT LICENSE
#
# COPYRIGHT (R) 2025 ARNELIFY. AUTHOR: TARON SARKISYAN
#
# PERMISSION IS HEREBY GRANTED, FREE OF CHARGE, TO ANY PERSON OBTAINING A COPY
# OF THIS SOFTWARE AND ASSOCIATED DOCUMENTATION FILES (THE "SOFTWARE"), TO DEAL
# IN THE SOFTWARE WITHOUT RESTRICTION, INCLUDING WITHOUT LIMITATION THE RIGHTS
# TO USE, COPY, MODIFY, MERGE, PUBLISH, DISTRIBUTE, SUBLICENSE, AND/OR SELL
# COPIES OF THE SOFTWARE, AND TO PERMIT PERSONS TO WHOM THE SOFTWARE IS
# FURNISHED TO DO SO, SUBJECT TO THE FOLLOWING CONDITIONS:
#
# THE ABOVE COPYRIGHT NOTICE AND THIS PERMISSION NOTICE SHALL BE INCLUDED IN ALL
# COPIES OR SUBSTANTIAL PORTIONS OF THE SOFTWARE.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import signal
import subprocess
import threading

from .env.index import Env
from ...logger.index import Logger

class Watcher:
  def __init__(self) -> None:
    self.pid: int = -1

  def apply(self, envPath: str) -> None:
    savePath = os.path.abspath('./src/core/env/index.py')
    raw: str = Env.read(envPath)
    data: dict = Env.parse(raw)
    sources: str = Env.sources(data)
    Env.save(savePath, sources)

  def build(self, watchPath, serverPath) -> None:
    buildPath = os.path.dirname(serverPath)
    if not os.path.exists(buildPath):
      os.makedirs(buildPath)
    srcPath: str = os.path.dirname(watchPath)
    os.system("make -C " + srcPath + " build")

  def start(self, watchPath) -> None:
    self.pid = os.fork()
    isSuccess = self.pid == 0
    isError = 0 > 0

    if isSuccess:
      os.execlp('python', 'python', str(watchPath))
    elif isError:
      print("Can't create child process.")
      exit(1)

  def close(self) -> None:
    if self.pid > 0:
      os.kill(self.pid, signal.SIGTERM)
      os.waitpid(self.pid, 0)
      self.pid = -1

  def watch(self, watchPath) -> None:
    srcPath: str = os.path.dirname(watchPath)
    def watcher():
      command = f"inotifywait -m -q -r -e modify --exclude 'src/core/env|src/storage' {srcPath}"
      inotify_pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

      if inotify_pipe is None:
        Logger.danger("Can't start watcher.")
        exit(1)

      while True:
        output = inotify_pipe.stdout.readline()
        if output:
          self.close()
          self.start(watchPath)

    thread = threading.Thread(target=watcher)
    thread.start()
    thread.join()