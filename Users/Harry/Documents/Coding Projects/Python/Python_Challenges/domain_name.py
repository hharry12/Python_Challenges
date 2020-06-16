def domain_name(url):

    if url.find("www.") != -1:
        return url[url.find("www.") + 4 : url[url.find("www.") + 4 : -1].find(".") + url.find("www.") + 4]
        

    elif url.find("//") != -1:
        return url[url.find("/") + 2 : url.find(".")]
        
    else:
        return url[0 : url.find(".")]
        
print(domain_name("https://www.indeed.co.uk/jobs?as_and&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&as_src&salary&radius=25&l=London&fromage=any&limit=10&sort=date&psf=advsrch&from=advancedsearch&vjk=3e9525b763efca68"))