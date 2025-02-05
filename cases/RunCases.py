from common.Utils import BlogDriver
from cases import BlogLogin
from cases import BlogList
from cases import BlogDetail
if __name__ == "__main__":
    BlogLogin.BlogLogin().loginSucTest()
    BlogList.BlogList().ListTest()
    BlogDetail.BlogDetail().DetailCheck()
    BlogDriver.driver.quit()