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

import json
import os

from ....logger.index import Logger

class Env:
  @staticmethod
  def read(envPath: str) -> str:
    try:
      with open(envPath, 'r', encoding='utf-8') as file:
        content = file.read()
      return content
    except Exception as e:
      Logger.danger(f"Error opening file: {envPath}\n")
      exit(1)

  @staticmethod
  def parse(raw: str) -> dict:
    data = {}
    lines = raw.splitlines()

    for line in lines:
      line = line.strip()
      if not line or line[0] == '#':
        continue
      if '=' not in line:
        continue

      key, value = line.split('=', 1)
      key = key.strip()
      value = value.strip()

      if key and value:
        data[key] = value

    return data

  @staticmethod
  def sources(data) -> None:
    sources = json.dumps(data)
    return "env = " + sources

  @staticmethod
  def save(envPath: str, sources: str) -> None:
    outDir: str = os.path.dirname(envPath)
    os.makedirs(outDir, exist_ok=True)
    try:
      with open(envPath, "w", encoding="utf-8") as file:
        file.write(sources)
    except Exception as e:
      Logger.danger(f"Error saving file: {envPath}\n")
      exit(1)