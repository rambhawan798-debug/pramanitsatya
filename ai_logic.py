# Yeh tisre charan ka AI logik hai: ai_logik.py

def generate_response(text):
    text_lower = text.lower()

    #Agar user ne hello ya hi bola
    if "hello" in text_lower or "hi" in text_lower:
        return "Namaste ram bhawan bhai! main aapka AI assistant hoon,boliye kya madad karoon"

    # Agar haal-chaal pucha
    elif "kaise ho" in text_lower:
        return "main aapki yeh baat sun li hai aur samajh li hai: " + text

    # Default jawab  agar kuch aur bola
    else:
        return "Maine aapki yeh baat sun li hai aur samajh li hai: " + text

# test karne ke liye chota as code
if __name__ == "__main__":
   user_input = input("Kuch boliye ya type kijiye: ")
   jawab = generate_response(user_input)
   print(jawab)