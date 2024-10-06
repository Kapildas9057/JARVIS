
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "eQiMutzDFLiUdubguHtbstfx9ZvFy7UGd6Yq2dd-2gUqXbr6xQXIgOfmU_3my5GXCV8ZcQ",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSq1rwXkH-COpNtmlWcQldmgSw5M7cj1gxUvnghNRmF3XZ0JIAg10tzqo8NlUEAA",
    "__Secure-1PSIDCC": "ABTWhQEP2rZBSw4odUPxit_Pf3RzJx0g-heOE5E7r-FxwSnEOof29lgSTG0NeG-FRNOe2mvLgA",
}

bard = BardCookies(cookie_dict=cookie_dict)
print(bard.get_answer("WHAT MODEL ARE YOU USING?")['content'])