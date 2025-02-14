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

import sys

class Logger:
    @staticmethod
    def log(message, color, replace):
        if replace:
            sys.stdout.write("\r" + " " * replace + "\r")
            sys.stdout.flush()

        sys.stdout.write(f"{color}[Arnelify POD]: {message}\033[0m")
        sys.stdout.flush()

    @staticmethod
    def primary(message, replace=0):
        Logger.log(message, "\033[0m", replace)

    @staticmethod
    def success(message, replace=0):
        Logger.log(message, "\033[32m", replace)

    @staticmethod
    def warning(message, replace=0):
        Logger.log(message, "\033[33m", replace)

    @staticmethod
    def danger(message, replace=0):
        Logger.log(message, "\033[31m", replace)