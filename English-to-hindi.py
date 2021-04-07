# importing the module
from englisttohindi.englisttohindi import EngtoHindi

# message to be translated
message = "Yes, My Name is Anjesh Singh"

# without creating object
print(EngtoHindi(message).convert)

# creating a EngtoHindi() object
res = EngtoHindi(message)

# displaying the translation
print(res.convert)

