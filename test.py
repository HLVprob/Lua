
def check_password():
    secret = "MoonSec_V6_Is_Unbreakable!"
    print("=== MOONSEC CRACKME CHALLENGE ===")
    user_input = input("Enter the secret key to unlock: ")
    
    if user_input == secret:
        print(">> [SUCCESS] HOLY SHIT! YOU CRACKED IT! <<")
        print(">> The flag is: CTF{M00N_S3C_T1T4N_PWN3D}")
    else:
        print(">> [FAIL] ACCESS DENIED. GET LOST!")

if __name__ == "__main__":
    check_password()
    
