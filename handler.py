# Max Fierro
# maxfierro@berkeley.edu
# 11/22/2022

# See https://docs.python-zeep.org/en/master/
import zeep
import os


WSDL = "http://webreports.berkeley.edu/webreports?wsdl"
FILES = os.path.join(os.getcwd(), "files")
KEYS = os.path.join(FILES, "keys")
RELEVANCE = os.path.join(FILES, "relevance")
OUT = os.path.join(FILES, "response")


class Keys:
    def __init__(self, keyfile: str):
        with open(keyfile) as f:
            keys = [line for line in f]
            self.user = keys[0].strip()
            self.password = keys[1].strip()


def relevance_statement(filepath: str) -> str:
    relevance_stmt = ""
    with open(filepath) as expr_file:
        for line in expr_file: relevance_stmt += line
    return relevance_stmt

def get_relevance_result(wsdl: str, expr: str, user: str, pswd: str) -> list:
    client = zeep.Client(wsdl = wsdl)
    response = client.service.GetRelevanceResult(expr, user, pswd)
    return response

def write_response(response: list, to_filepath: str, delimiter: str) -> None:
    with open(to_filepath, "w") as out:
        for element in response:
            out.write(element)
            out.write(delimiter)


if __name__ == "__main__":
    keys = Keys(keyfile = KEYS)
    relevance = relevance_statement(RELEVANCE)
    response = get_relevance_result(WSDL, relevance, keys.user, keys.password)
    write_response(response, OUT, "\n")
