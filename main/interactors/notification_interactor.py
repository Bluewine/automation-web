from libs.interactor.interactor import Interactor
from main.models import Notifications


class SetNotificationInteractor(Interactor):
    def run(self):
        data = self.context.data
        exception = None
        print("data from Notif Interactor", data)

        try:
            user = data['user']
            msg = data['message']
            link = data['link']
            status = data['status']
            type = data['type']

            notification = Notifications()
            notification.status = status
            notification.link = link
            notification.user = user
            notification.message = msg
            notification.type = type

            notification.save()

            if link == "__self__":
                notification.link = f'/notifications/view/{notification.pk}'
                notification.save()
        except Exception as e:
            exception = e
        finally:
            self.context.exception = exception
