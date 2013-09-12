import sys

class Job:
	def __init__(self, weight, length):
		self.weight = weight
		self.length = length
		self.m1 = self.weight - self.length
		self.m2 = 1.0*self.weight / self.length
	def __repr__(self):
		return "Job(w: %s; l: %s; w-l: %s; w/l: %.2f)" % (self.weight, self.length, self.m1, self.m2)

def score(jobs):
	time,score=0,0
	for job in jobs:
		time += job.length
		score += time*job.weight
	return score

input_list=[x.strip().split() for x in file(sys.argv[1],"r")]
jobs = [Job(int(w),int(l)) for (w,l) in input_list[1:]]

jobs = sorted(jobs, key=lambda job: job.weight, reverse=True)
prob1 = sorted(jobs, key=lambda job: job.m1, reverse=True)
prob2 = sorted(jobs, key=lambda job: job.m2, reverse=True)

print score(prob1)
print score(prob2)


