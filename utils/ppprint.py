import pprint, json
import json
import pprint

def print_p(data, log=False):
    """
    Print the given data with human-friendly formatting.

    Args:
        data: The data to be printed. It can be either a bytes object or a JSON-formatted string.
        log: A boolean flag indicating whether to write the data to a file.

    Returns:
        None
    """

    if isinstance(data, bytes):
        data = data.decode('utf-8')
    elif isinstance(data, str):
        data = json.loads(data)

    # print json to screen with human-friendly formatting
    pprint.pprint(data, compact=True)

    # write json to file with human-friendly formatting
    pretty_json_str = pprint.pformat(data, compact=True)

    if log:
        with open('output.json', 'a+') as f:
            f.write(pretty_json_str)