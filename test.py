from openai import OpenAI
from config import apikey
client = OpenAI(api_key= apikey)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write a resignation letter to my boss\n"
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


"""

[Your Name]
[Your Address]
[City, State, ZIP Code]
[Email Address]
[Phone Number]
[Date]

[Recipient's Name]
[Recipient's Designation]
[Company Name]
[Company Address]
[City, State, ZIP Code]

Dear [Recipient's Name],

I hope this letter finds you well. I am writing to officially tender my resignation from my position as [Your Job Title] at [Company Name], effective [Last Working Day], in accordance with the notice period stated in my employment contract.

Firstly, I would like to express my gratitude for the opportunities and experiences I have gained during my tenure at [Company Name]. The past [Duration of Employment] has been personally fulfilling and professionally enriching. I have had the privilege of working with a team of talented individuals who have constantly motivated me to push my boundaries and excel in my role.

However, after careful consideration and personal reflection, I have come to the decision that it is time for me to embark on a new career path. This decision was not made easily, as I have thoroughly enjoyed my time at [Company Name] and appreciate the support, guidance, and trust you have shown me throughout my employment.

I want to assure you that I will do everything in my capacity
"""