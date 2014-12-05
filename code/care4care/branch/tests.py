from django.test import TestCase
from django.utils import timezone
from branch.models import Branch, BranchMembers, Demand, Offer, DemandProposition
from main.models import User 

# Create your tests here.

class BranchTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="first_test", last_name="last_test",\
        username="username_test",birth_date=timezone.now(),how_found=0,\
        email="test@test.com", password="test", is_staff=True, is_verified=True)

		user = User.objects.get(first_name="first_test") 

		Branch.objects.create(name="test_name", creator=user)

		branch = Branch.objects.get(name="test_name")


	def test_branch_exist(self):
		branch = Branch.objects.get(name="test_name")
		self.assertIsNotNone(branch)

	def test_add_member_in_branch(self):
		branch = Branch.objects.get(name="test_name")
		user = User.objects.get(first_name="first_test")
		BranchMembers.objects.create(user=user, branch=branch, joined=timezone.now(), is_admin=False)
		res = branch.members.filter(id=user.id).exists()
		self.assertEqual(res, True)

class BranchLeaveTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="first_test", last_name="last_test",\
        username="username_test",birth_date=timezone.now(),how_found=0,\
        email="test@test.com", password="test", is_staff=True, is_verified=True)

		user = User.objects.get(first_name="first_test") 

		Branch.objects.create(name="test_name", creator=user)

		branch = Branch.objects.get(name="test_name")

	def test_leave_branch(self):
		branch = Branch.objects.get(name="test_name")
		user = User.objects.get(first_name="first_test")
		BranchMembers.objects.create(user=user, branch=branch, joined=timezone.now(), is_admin=False)
		res = branch.members.filter(id=user.id).all
		BranchMembers.objects.filter(user=user).delete()
		res2 = branch.members.filter(id=user.id).all
		self.assertNotEqual(res,res2)


class DemandTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="first_test", last_name="last_test",\
        username="username_test",birth_date=timezone.now(),how_found=0,\
        email="test@test.com", password="test", is_staff=True, is_verified=True)
		user = User.objects.get(first_name="first_test") 
		Branch.objects.create(name="test_name", creator=user)
		branch = Branch.objects.get(name="test_name")
		Demand.objects.create(title="test", estimated_time=10, date=timezone.now(), branch=branch)

	def test_branch_exist(self):
		demand = Demand.objects.filter(title="test")
		self.assertIsNotNone(demand)

	def test_create_demand_proposition(self):
		user = User.objects.get(first_name="first_test") 
		demand = Demand.objects.get(title="test")
		DemandProposition.objects.create(user=user,demand=demand)
		self.assertIsNotNone(demand.volunteers)

class DemandTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="first_test", last_name="last_test",\
        username="username_test",birth_date=timezone.now(),how_found=0,\
        email="test@test.com", password="test", is_staff=True, is_verified=True)
		user = User.objects.get(first_name="first_test") 
		Branch.objects.create(name="test_name", creator=user)
		branch = Branch.objects.get(name="test_name")
		Demand.objects.create(title="test", estimated_time=10, date=timezone.now(), branch=branch)

	def test_branch_exist(self):
		demand = Demand.objects.filter(title="test")
		self.assertIsNotNone(demand)


	def test_create_demand_proposition(self):
		user = User.objects.get(first_name="first_test") 
		demand = Demand.objects.get(title="test")
		DemandProposition.objects.create(user=user,demand=demand)
		self.assertIsNotNone(demand.volunteers)

class OfferTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="first_test", last_name="last_test",\
        username="username_test",birth_date=timezone.now(),how_found=0,\
        email="test@test.com", password="test", is_staff=True, is_verified=True)
		user = User.objects.get(first_name="first_test") 
		Branch.objects.create(name="test_name", creator=user)
		branch = Branch.objects.get(name="test_name")
		Offer.objects.create(date=timezone.now(), branch=branch)

	def test_branch_exist(self):
		branch = Branch.objects.get(name="test_name")
		offer = Offer.objects.get(branch=branch)
		self.assertIsNotNone(offer)

