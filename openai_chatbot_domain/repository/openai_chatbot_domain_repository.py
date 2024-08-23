from abc import abstractmethod, ABC

class OpenaiChatbotDomainRepository(ABC):
    @abstractmethod
    def generateRecipe(self, userSendMessage):
        pass

    @abstractmethod
    def getGeneratedVoice(self, chatbotMessage, voiceActor):
        pass