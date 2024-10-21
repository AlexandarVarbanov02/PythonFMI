from typing import List


def emails_shortener(emails: List[str]):
    email_dict = dict()
    for email in emails:
        name, domain = email.split('@')
        domain = '@' + domain
        if domain in email_dict:
            email_dict[domain].append(name)
        else:
            email_dict[domain] = list()
            email_dict[domain].append(name)

    result = set()
    for key, value in email_dict.items():
        if len(value) > 1:
            result.add(f"{{{','.join(value)}}}{key}")
        else:
            result.add(f"{''.join(value)}{key}")
    return result


assert emails_shortener([
    "pesho@abv.bg",
    "gosho@abv.bg",
    "sasho@abv.bg",
]) == {
    "{pesho,gosho,sasho}@abv.bg"
}

assert emails_shortener([
    "tinko@fmi.uni-sofia.bg",
    "minko@fmi.uni-sofia.bg",
    "pesho@pesho.org",
]) == {
    "{tinko,minko}@fmi.uni-sofia.bg",
    "pesho@pesho.org",
}

assert emails_shortener([
    "toi_e@pesho.org",
    "golemiq@cyb.org",
]) == {
    "toi_e@pesho.org",
    "golemiq@cyb.org",
}
