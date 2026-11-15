
import dns.resolver

def check_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(answer) for answer in answers]
    except dns.resolver.NoAnswer:
        return []
    except Exception as error:
        return [f"Lookup error: {error}"]

def troubleshoot(domain):
    print(f"\nMailSleuth Report for: {domain}")
    print("-" * 45)

    # Check mail server
    mx = check_record(domain, "MX")
    print("\nMX Records:", mx or "Not found")

    # Check SPF policy
    txt_records = check_record(domain, "TXT")
    spf = [r for r in txt_records if "v=spf1" in r.lower()]
    print("\nSPF Records:", spf or "Not found")

    # Check DMARC policy
    dmarc = check_record("_dmarc." + domain, "TXT")
    print("\nDMARC Records:", dmarc or "Not found")

    # Check the common DKIM selector "default"
    dkim = check_record("default._domainkey." + domain, "TXT")
    print("\nDKIM (default selector):", dkim or "Not found")

    print("\nTroubleshooting suggestions:")
    if not mx:
        print("- Verify that the domain has the correct MX records.")
    if not spf:
        print("- Check whether the domain needs a valid SPF policy.")
    if not dmarc:
        print("- Check whether a DMARC policy is configured.")
    if not dkim:
        print("- Verify the DKIM selector and public key with the administrator.")

    print("\nCheck completed.")

if __name__ == "__main__":
    domain = input("Enter a domain (e.g. gmail.com): ").strip()
    if domain:
        troubleshoot(domain)
    else:
        print("Please enter a domain.")
