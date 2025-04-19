def create_vcard():
    # Accept contact details from the user
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    # Create the vCard content
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
END:VCARD
"""

    # Write the vCard content to a .vcf file
    with open(f"{name}.vcf", "w") as vcard_file:
        vcard_file.write(vcard_content)

    print(f"vCard for {name} created successfully as {name}.vcf!")

create_vcard()