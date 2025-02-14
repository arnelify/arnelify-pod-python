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
import sys

from .watcher.index import Watcher
from .plant.index import Plant
from ..logger.index import Logger

class Boot:
  @staticmethod
  def setup() -> None:
    Logger.warning("Installing framework...\n")

    Plant.mkdir("./src/app/middleware")
    Plant.mkdir("./src/app/repositories")
    Plant.mkdir("./src/app/requests")
    Plant.mkdir("./src/app/services")
    Plant.mkdir("./src/app/translations")
    Plant.mkdir("./src/database/factories")
    Plant.mkdir("./src/database/migrations")
    Plant.mkdir("./src/database/seeds")
    Plant.mkdir("./src/tests")

    Logger.warning("Installing packages...\n")
    Logger.success("Successfully!\n")

  @staticmethod
  def build() -> None:
    envPath: str = os.path.abspath(".env")
    watchPath: str = os.path.abspath("src/server.py")
    serverPath: str = os.path.abspath("pod/server")

    watcher: Watcher = Watcher()        
    watcher.apply(envPath)
    watcher.build(watchPath, serverPath)

  @staticmethod
  def watch() -> None:
    envPath: str = os.path.abspath(".env")
    watchPath: str = os.path.abspath("src/watch.py")

    watcher: Watcher = Watcher()
    watcher.apply(envPath)
    watcher.start(watchPath)
    watcher.watch(watchPath)
    
  @staticmethod
  def migrate() -> None:
    print("migrate")
    
  @staticmethod
  def seed() -> None:
    print("seed")
    
def main() -> int:
  for i in range(0, len(sys.argv)):

    isSetup: bool = sys.argv[i] == "setup"
    if isSetup:
      Boot.setup()
      break
    
    isBuild: bool = sys.argv[i] == "build"
    if isBuild:
      Boot.build()
      break

    isWatch: bool = sys.argv[i] == "watch"
    if isWatch:
      Boot.watch()
      break
      
    isMigrate: bool = sys.argv[i] == "migrate"
    if isMigrate:
      Boot.migrate()
      break

    isSeed: bool = sys.argv[i] == "seed"
    if isSeed:
      Boot.seed()
      break

  return 0

if __name__ == "__main__":
    main()