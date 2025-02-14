from core.logger.index import Logger
import json

class SecondService:
  def welcome(ctx):
    params = ctx["params"]
    numbers = params["numbers"]

    result = sum(numbers)
    res = {"code": 200, "success": "Welcome to Arnelify POD framework."}
    joined = " + ".join(map(str, numbers))
    Logger.primary(f"Second: Hi, First! The result of {joined} is = {result}.\n")

    resString = json.dumps(res, separators=(',', ':'))
    Logger.primary(f"Second: Here's your response: {resString}\n")

    return {
      "code": 200,
      "success": { "result": result, "response": res }
    }