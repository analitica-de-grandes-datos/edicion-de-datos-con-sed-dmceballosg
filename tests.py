import os

expected = r"""2013-03-12,A,1,100.0
2013-12-05,A,1,100.0
2013-02-25,B,2,200.0
2013-04-04,\N,1,\N
2013-06-21,\N,\N,\N
2014-06-13,A,\N,\N
2014-05-12,C,\N,\N
2014-09-05,\N,3,150.1
2014-05-12,A,2,\N
2013-02-28,C,\N,\N
2013-08-02,A,2,100.0
2014-09-01,A,3,100.4""".split(
    "\n"
)


if os.system("bash question.sh data.csv > output.csv") != 0:
    raise Exception


with open("output.csv", "r", encoding="utf8") as f:
    lines = f.readlines()

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")


lines = [line.strip().replace("\n", "") for line in lines]

for solution, expected in zip(lines, expected):
    assert solution == expected, f"Expected: {expected}\nGot: {solution}"
