import unittest
from unittest import mock
from githubapi import printGithubStats


class TestGithubApiTest(unittest.TestCase):

    @mock.patch('githubapi.printGithubStats', return_value=['Repo: ckubelle Number of commits: 3', 'Repo: Complexity Number of commits: 30', 'Repo: Convolutional-Neural-Network-CIFAR-10 Number of commits: 3', 'Repo: DesignPatternLab Number of commits: 2', 'Repo: firebasetest Number of commits: 2', 'Repo: GEDCOM-Project Number of commits: 30', 'Repo: GithubAPI567 Number of commits: 7', 'Repo: helloworld Number of commits: 3', 'Repo: HW3 Number of commits: 3', 'Repo: HW4 Number of commits: 6', 'Repo: HW5 Number of commits: 9', 'Repo: morseCode Number of commits: 7', 'Repo: Node.jsAppLab Number of commits: 3', 'Repo: SSW345TeamProject Number of commits: 8', 'Repo: SSW567-HW1 Number of commits: 3', 'Repo: stockFinder Number of commits: 10', 'Repo: TestSurveySystem Number of commits: 30', 'Repo: TestTriangle-SSW567 Number of commits: 9'])
    def testMyself(self, mock_get):
        expectedOutput = ['Repo: ckubelle Number of commits: 3', 'Repo: Complexity Number of commits: 30', 'Repo: Convolutional-Neural-Network-CIFAR-10 Number of commits: 3', 'Repo: DesignPatternLab Number of commits: 2', 'Repo: firebasetest Number of commits: 2', 'Repo: GEDCOM-Project Number of commits: 30', 'Repo: GithubAPI567 Number of commits: 7', 'Repo: helloworld Number of commits: 3', 'Repo: HW3 Number of commits: 3', 'Repo: HW4 Number of commits: 6', 'Repo: HW5 Number of commits: 9', 'Repo: morseCode Number of commits: 7', 'Repo: Node.jsAppLab Number of commits: 3', 'Repo: SSW345TeamProject Number of commits: 8', 'Repo: SSW567-HW1 Number of commits: 3', 'Repo: stockFinder Number of commits: 10', 'Repo: TestSurveySystem Number of commits: 30', 'Repo: TestTriangle-SSW567 Number of commits: 9']
        self.assertEqual(printGithubStats('ckubelle'), expectedOutput)

    @mock.patch('githubapi.printGithubStats', return_value=[])
    def testInvalidUser(self, mock_get):
        self.assertEqual(printGithubStats('kjafdanberg'), [])



if __name__ == '__main__':

    unittest.main()
