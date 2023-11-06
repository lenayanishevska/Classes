from Countries.Country import Country

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina1 = bosnia.add(herzegovina)
bosnia_herzegovina2 = bosnia + herzegovina

print(bosnia_herzegovina1)
print(bosnia_herzegovina2)

