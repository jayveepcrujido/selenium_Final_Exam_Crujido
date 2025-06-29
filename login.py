from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

def login_admin(): #define function for logging in admin
    driver.get("https://localhost/ocss/admin_login.php")
    time.sleep(2)

    try: #the window asks if you want to advance even if the site is not secure
        advanced = driver.find_element(By.ID, "details-button")
        advanced.click()
        time.sleep(1)
        
        try:
            proceed_link = driver.find_element(By.ID, "proceed-link")
            proceed_link.click()
            time.sleep(1)
        except NoSuchElementException:
            print("Proceed link not found. Skipping...")
    except NoSuchElementException:
        print("Advanced button not found. Skipping...")

    txtEmail = driver.find_element(By.NAME, "admin_username") #enter username
    txtEmail.send_keys("admin")
    time.sleep(1)

    txtPwd = driver.find_element(By.NAME, "admin_pass") #enter password
    txtPwd.send_keys("admin")
    time.sleep(1)

    login_button = driver.find_element(By.NAME, "admin_login") #click login button
    login_button.click()
    time.sleep(2)




def login_faculty():
    driver.get("https://localhost/ocss/index.php")
    time.sleep(3)

    txtEmail = driver.find_element(By.NAME, "user_email") #enter username
    txtEmail.send_keys("jd@gmail.com")
    time.sleep(1)

    txtPwd = driver.find_element(By.NAME, "user_pass") #enter password
    txtPwd.send_keys("juan123")
    time.sleep(1)

    login_button = driver.find_element(By.NAME, "Login") #click login button
    login_button.click()
    time.sleep(3)

    logout = driver.find_element(By.ID, "logout") #click logout button
    logout.click()
    time.sleep(2)

def register_faculty():
    menu = driver.find_element(By.ID, "menu") #click sidebar
    menu.click()
    time.sleep(2)

    add_faculty = driver.find_element(By.ID, "add faculty") #click the modal for adding faculty
    add_faculty.click()
    time.sleep(2)

    fname = driver.find_element(By.NAME, "fname") #enter first name
    fname.send_keys("Juan")
    time.sleep(1)

    dateHired = driver.find_element(By.NAME, "date_hired") #enter date hired
    dateHired.send_keys("12/12/2002")
    time.sleep(1)

    status = driver.find_element(By.ID, "status") #enter status dropdown
    status.click()
    time.sleep(1)

    choice = driver.find_element(By.ID, "part-time") #click part-time option
    choice.click()
    time.sleep(1)

    field = driver.find_element(By.NAME, "background_field") #enter background field
    field.send_keys("BSIT")
    time.sleep(1)

    address = driver.find_element(By.NAME, "address") #enter address
    address.send_keys("Brgy. Sildora")
    time.sleep(1)

    contact = driver.find_element(By.NAME, "contact_no") #enter contact number
    contact.send_keys("0987654321")
    time.sleep(1)

    email = driver.find_element(By.NAME, "email") #enter invalid email
    email.send_keys("jd")
    time.sleep(1)

    passw = driver.find_element(By.NAME, "pass") #enter password
    passw.send_keys("juan123")
    time.sleep(1)

    add = driver.find_element(By.NAME, "register_faculty") #the website should not accept the email is invalid
    add.click()
    time.sleep(3)

    empNum = driver.find_element(By.NAME, "emp_number") #enter id 
    empNum.send_keys("098765")
    time.sleep(1)

    add = driver.find_element(By.NAME, "register_faculty") #filter errors
    add.click()
    time.sleep(3)

    email = driver.find_element(By.NAME, "email") 
    email.clear()
    email.send_keys("jd@gmail.com")
    time.sleep(1)

    add = driver.find_element(By.NAME, "register_faculty") #save faculty
    add.click()
    time.sleep(2)

    menu = driver.find_element(By.ID, "menu") #click sidebar menu
    menu.click()
    time.sleep(1)

    logout = driver.find_element(By.ID, "logout") #logout
    logout.click()
    time.sleep(2)


def add_subject():
    menu = driver.find_element(By.ID, "menu") #click sidebar menu
    menu.click()
    time.sleep(2)

    add_subj = driver.find_element(By.ID, "add subject") #click modal for adding subject
    add_subj.click()
    time.sleep(2)

    code = driver.find_element(By.NAME, "subject_code") #enter subject code
    code.send_keys("COMP-001")
    time.sleep(1)

    desc = driver.find_element(By.NAME, "subject_description") #enter description
    desc.send_keys("Introduction to Computing")
    time.sleep(1)

    unit = driver.find_element(By.ID, "unit") #enter unit
    unit.click()
    time.sleep(1)

    unit_no = driver.find_element(By.ID, "2") 
    unit_no.click()
    time.sleep(1)

    lecture = driver.find_element(By.ID, "lecture") #enter lecture number
    lecture.click()
    time.sleep(1)

    lecture_no = driver.find_element(By.ID, "lect3") 
    lecture_no.click()
    time.sleep(1)

    lecture = driver.find_element(By.ID, "laboratory") #enter lab number
    lecture.click()
    time.sleep(1)

    lab_no = driver.find_element(By.ID, "lab2") 
    lab_no.click()
    time.sleep(1)

    submit_subj = driver.find_element(By.NAME, "add") #click add
    submit_subj.click()
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

def add_room():
    menu = driver.find_element(By.ID, "menu") #click sidebar
    menu.click()
    time.sleep(2)

    add_room = driver.find_element(By.ID, "add room") #click modal for adding room
    add_room.click()
    time.sleep(1)

    room = driver.find_element(By.NAME, "room") #add room number
    room.send_keys("Room 110")
    time.sleep(1)

    add = driver.find_element(By.NAME, "add_room") #click add room
    add.click()
    time.sleep(3)

def create_schedule():
    menu = driver.find_element(By.ID, "menu") #click sidebar
    menu.click()
    time.sleep(2)

    create_sched = driver.find_element(By.ID, "ceate_sched") #click create schedule
    create_sched.click()
    time.sleep(1)

    desc = driver.find_element(By.ID, "subject_description") 
    desc.click()
    time.sleep(1)

    number = driver.find_element(By.ID, "13") #choose the introduction to computing subject
    number.click()
    time.sleep(1)

    day = driver.find_element(By.ID, "day_description") 
    day.click()
    time.sleep(1)

    select_day = driver.find_element(By.ID, "day_11") #select day
    select_day.click()
    time.sleep(1)

    timed = driver.find_element(By.ID, "time_description") 
    timed.click()
    time.sleep(1)

    select_time = driver.find_element(By.ID, "time_10") #select time
    select_time.click()
    time.sleep(1)

    room = driver.find_element(By.ID, "room_description") 
    room.click()
    time.sleep(1)

    select_room = driver.find_element(By.ID, "room_11") #select room
    select_room.click()
    time.sleep(1)

    prof = driver.find_element(By.ID, "fname") 
    prof.click()
    time.sleep(1)

    select_day = driver.find_element(By.ID, "name_47") #select faculty
    select_day.click()
    time.sleep(1)

    save = driver.find_element(By.NAME, "add_schedule") 
    save.click()
    time.sleep(1)

    time.sleep(3)

#call all the functions and run
login_admin()
register_faculty()
login_faculty()
login_admin()
add_subject()
add_room()
create_schedule()
login_faculty()