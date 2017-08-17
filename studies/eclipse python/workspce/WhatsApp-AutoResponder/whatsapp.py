from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display  
import os
import time
import chatbat
import classification
import sys;
#===============================================================================
# reload(sys);
# sys.setdefaultencoding("utf8")
#===============================================================================

#===============================================================================
# display = Display(visible=1, size=(1920, 1080))
# display.start()
#===============================================================================

#last msg for identifying #lastMsg

class Whatsapp:

	def __init__(self):
	#	binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
	#	fp = webdriver.FirefoxProfile()
		#=======================================================================
		# firefox_binary=binary, firefox_profile=fp
		#=======================================================================
		self.browser = webdriver.Firefox()
		self.lastMsg=str('')

	def sendMessage(self, people):
		#msg = "Hello, Ashish is currently unavailable, Please leave your message after next beep ....*Beep* :P "
		
		for name in people:
			try:
				print(self.lastMsg)
				elem = self.browser.find_element_by_xpath(
				'//span[contains(text(),"%s")]'%name
				)			
				elem.click()
				elem1 = self.browser.find_elements_by_class_name('input')
				oMsg=self.browser.find_elements_by_class_name('msg')
				msg = str(oMsg[len(oMsg)-1].text.split('\n')[0])
				if msg != self.lastMsg:
					try:
						if (msg.index('male') or msg.index('female')):
							self.lastMsg = classification.genderText(msg.split(' ')[0])
						else:
							self.lastMsg = str(chatbat.chatbotResponse(msg))
					except:
						self.lastMsg = str(chatbat.chatbotResponse(msg))
					elem1[0].send_keys(self.lastMsg)
					self.browser.find_element_by_class_name('compose-btn-send').click()
			except:
				print('Unable to read name')

	def login(self):
		self.browser.get('http://web.whatsapp.com')
		#input('Press any key whenever you are ready')

	def read(self):

		while(1):

			#self.browser.get('http://web.whatsapp.com')
			#time.sleep(15)
			try:
							
				try:
					page = self.browser.page_source
				except:
					print("Unable to load page")
					
				tree = html.fromstring(page)

				unread = tree.xpath(
					'//div[contains(@class, "infinite-list-item")]/div[1]/div[contains(@class, "unread chat")]//div[contains(@class, "chat-body")]/div[contains(@class, "chat-main")]/div[contains(@class, "chat-title")]/span/@title'
					)
				print('You have unread message from :')
				if(len(unread) == 0):
					try:
						unread = [self.browser.find_elements_by_class_name('active')[0].find_element_by_class_name('chat-title').text]
					except:
						print("Unable to load page")
				else:
					self.lastMsg =str('')
				for person in unread:
					print(person)

				self.sendMessage(unread)
			except:
				print("Unable to execute notification")
			time.sleep(3)  