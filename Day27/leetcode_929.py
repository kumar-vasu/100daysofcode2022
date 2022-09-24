class Solution:
     def numUniqueEmails(self, emails: List[str]) -> int:
            st = set()
            for email in emails:
                names = email.split("@")
                localname = names[0]
                domainname = names[1]
                if  domainname.endswith(".com") == False or localname.startswith("+"):
                    continue
                localname = localname.replace(".","")

                if "+" in localname:
                    index = localname.index("+")
                    localname = localname[0:index]
                st.add(localname+"@" + domainname)

            return len(st)