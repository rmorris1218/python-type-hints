from typing import Dict, List


def tags_to_list(tags: Dict) -> List[Dict[str, str]]:
    return [{"Key": k, "Value": v} for k, v in tags.items()]


if __name__ == "__main__":
    tags = tags_to_list(tags={"k": "v"})
    print("hello world")
