c, p = [int(x) for x in input().strip().split(" ")]

contributers = []
projects = []

for i in range(c):
    name, n_skills = [x for x in input().strip().split(" ")]
    skills = []
    for _ in range(int(n_skills)):
        skill, level = [x for x in input().strip().split(" ")]
        skills.append([skill, int(level)])

    contributers.append([name, skills])


for i in range(p):
    name, duration, score, deadline, num_roles = [x for x in input().strip().split(" ")]
    skills = []
    for _ in range(int(num_roles)):
        skill, level = [x for x in input().strip().split(" ")]
        skills.append([skill, int(level)])

    projects.append(
        [name, int(duration), int(score), int(deadline), int(num_roles), skills]
    )

projects = sorted(projects,key=lambda x: x[3])

count = 0
time = 0
res = []

for project in projects:

    roles = project[5]
    people = []
    for r in roles:
        req_role, req_level = r[0], r[1]
        for contri in contributers:
            name, skill = contri[0], contri[1]
            for s in skill:
                if  req_role==s[0] and s[1] >= req_level:
                    if not name in set(people):
                        people.append(name)
                        break
    if len(people) == len(roles):
        count += 1
        time += project[1]
        res.append([project[0], people])


print(count)
for val in res:
    print(val[0])
    print(" ".join(val[1]))
