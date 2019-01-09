#definiton of country
countries = ["spain", "france", "germany", "norway"]
capitals = ["madrid", "paris", "berlin", "oslo"]
europe = {"spain":"madrid", "france":"paris", "germany":"berlin", "norway":"oslo"}
print(europe)
print(europe.keys())
print(type(europe))
print(europe["germany"])
#adding value in dict. europe
europe["italy"] = "rome"
europe["poland"] = "wasow"
#check is italy in europe
print("poland" in europe)
print("italy" in europe)
print(europe)
#how to delet a key from dict europe
del(europe["poland"])
print(europe)
#dictionary of dictionaries
europe = {'spain':{'capital':'madrid', 'population':46.77},
          'france':{'capital':'paris', 'population':66.03},
          'germany':{'capital':'berlin', 'populatin':80.62}}

print(europe['france']['capital'])
data = {'capital':'rome', 'population':59.83}
#add data to dict europe
europe['italy'] = data
print(europe)


