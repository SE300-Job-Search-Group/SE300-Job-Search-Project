from companyMatch import CompanyMatch
from user import User

class JobMatch:

    def userMatch(self, user: User) -> float:
        # Extract user information
        user_skills = user.getSkills()
        user_salary_range = user.getSalaryRange()
        user_location = user.getLocation()

        # Extract job information
        job_skills = self.getTags()
        job_salary_range = self.getSalaryRange()
        job_location = self.getLocation()

        # Match user skills with job tags
        skill_match = len(set(user_skills) & set(job_skills)) / len(set(user_skills))

        # Match user salary range with job salary range
        salary_match = min(user_salary_range[1], job_salary_range[1]) - max(user_salary_range[0], job_salary_range[0])
        salary_match = max(0, salary_match) / (user_salary_range[1] - user_salary_range[0])

        # Match user location with job location
        location_match = user_location.calculateDistance(job_location)

        # Calculate overall match rating (CHANGE WEIGHTS)
        match_rating = 0.4 * skill_match + 0.4 * salary_match + 0.2 * (1 - location_match)

        return match_rating
