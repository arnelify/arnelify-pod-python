from arnelify_server import ArnelifyServer
from arnelify_router import ArnelifyRouter

from core.env.index import env
from core.logger.index import Logger

from routes import routes
import json

def main():
  router: ArnelifyRouter = ArnelifyRouter()
  routes(router)

  server: ArnelifyServer = ArnelifyServer({
    "SERVER_ALLOW_EMPTY_FILES": env["SERVER_ALLOW_EMPTY_FILES"] == "true",
    "SERVER_BLOCK_SIZE_KB": int(env["SERVER_BLOCK_SIZE_KB"]),
    "SERVER_CHARSET": env["SERVER_CHARSET"],
    "SERVER_GZIP": env["SERVER_GZIP"] == "true",
    "SERVER_KEEP_EXTENSIONS": env["SERVER_KEEP_EXTENSIONS"] == "true",
    "SERVER_MAX_FIELDS": int(env["SERVER_MAX_FIELDS"]),
    "SERVER_MAX_FIELDS_SIZE_TOTAL_MB": int(env["SERVER_MAX_FIELDS_SIZE_TOTAL_MB"]),
    "SERVER_MAX_FILES": int(env["SERVER_MAX_FILES"]),
    "SERVER_MAX_FILES_SIZE_TOTAL_MB": int(env["SERVER_MAX_FILES_SIZE_TOTAL_MB"]),
    "SERVER_MAX_FILE_SIZE_MB": int(env["SERVER_MAX_FILE_SIZE_MB"]),
    "SERVER_PORT": int(env["SERVER_PORT"]),
    "SERVER_QUEUE_LIMIT": int(env["SERVER_QUEUE_LIMIT"]),
    "SERVER_UPLOAD_DIR": "src/storage/upload"
  })

  def handler(req: dict, res):
    method: str = req["_state"]["method"]
    path: str = req["_state"]["path"]

    routeOpt: dict | None = router.find(method, path)
    if not routeOpt:
      res.setCode(404)
      res.addBody(json.dumps({
        "code": 404,
        "error": "Not found."
      }, separators=(',', ':')))
      res.end()
      return
    
    res.setCode(200)
    route: dict = routeOpt
    controller: callable = router.getController(route["id"])
    response: dict | str = controller({"params": req})
  
    if not isinstance(response, dict):
      res.addBody(response)
      res.end()
      return

    if "code" in response:
      res.setCode(int(response["code"]))

    res.addBody(json.dumps(response, separators=(',', ':')))
    res.end()

  server.setHandler(handler)

  def callback(message: str, isError: bool):
    if isError:
      Logger.danger("Error: " + message + "\n")
      return
    
    Logger.success(message + "\n")

  server.start(callback)

if __name__ == "__main__":
    main()