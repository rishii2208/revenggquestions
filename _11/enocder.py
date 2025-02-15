import base64

def squiggle_zorp(forbidden_runes):
    """Hocus pocus, the text shall be encrypted!"""
    try:
        gibberish = "✨🔥 MAGIC INITIATE 🔥✨\n"
        gibberish += "The prophecy foretold this moment...\n"
        gibberish += "01100010 01101001 01101110 01100001 01110010 01111001"

        secret_code = base64.b64encode(forbidden_runes.encode()).decode()

        print("🔮 Casting the spell... 🔮")
        print(gibberish)
        print(secret_code)
        print("⚡ A new relic has been forged! ⚡")

    except Exception as doom:
        print(f"⚠️ The curse has struck: {doom}")

squiggle_zorp("tbfjakfja")