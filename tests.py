from django.test import TestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from apps.accounts.forms import RegistrationForm
from apps.accounts.views import *
from apps.exams.models import Exam, Test, Answer
from apps.questions.models import Question, Option
from apps.exams import views


class ExamTestCase(TestCase):
    """
    A selenium test for the exam app in my exam_site project.
    To view the full project visit https://github.com/abdulshukoorpk/Exam-Site
    
    """
    def setUp(self):
        """
        Initial method that is common to all test methods.
        This method runs before each test cases. 
        """
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(ExamTestCase, self).setUp()

    def tearDown(self):
        """
        Initial method that is common to all test methods.
        This method runs after each test cases. 
        """
        self.selenium.quit()
        super(ExamTestCase, self).tearDown()

    def test_5_question_display(self):
        """
        Test to check whether questions are displayed or not
        """

        print self.test_5_question_display.__doc__
        login_page = self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username = self.selenium.find_element_by_id('id_username')
        username.send_keys('testuser1')
        password = self.selenium.find_element_by_id('id_password')
        password.send_keys('test')
        self.selenium.find_element_by_xpath(
            '//input[@value = "Login"]').click()
        next_page = self.selenium.find_element_by_link_text(
            "Click to go to your Exam page").click()
        question_page = self.selenium.find_element_by_link_text(
            "exam2").click()

    def test_6_option_selection(self):
        """
        Test to check if user can select and submit answers
        """

        print self.test_6_option_selection.__doc__
        self.test_5_question_display()
        self.selenium.find_element_by_xpath('//input[@id = "option3"]').click()
        self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        self.selenium.find_element_by_xpath('//input[@id = "option1"]').click()
        self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()

    def test_7_result_page(self):
        self.test_6_option_selection()
        self.assertEquals(
            self.selenium.current_url, 'http://127.0.0.1:8000/exams/2/result'
        )
