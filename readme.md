# Assignment - A broken currywurst machine
Just another day at the Berlin office: you want to get a currywurst from the
famous currywurst machine, but something is different today: There is a note
on it reading
“Warning! I won’t return any change!”
You see your lunch going down the drain.. your precious currywurst! You know
that the only way to solve this is to fix it yourself.
## 1. A function
Fix the currywurst machine by re-programming functionality of the
return_coins() function. The currywurst costs 1.23 EUR, but you have only a
500 EUR banknote because you worked lots of night shifts. Being a good person
inside, you want to fix the machine for all your colleagues too, so it works with
any amount inserted. Also, you don’t want to carry a pocket full of coins, so it
should return the lowest amount of coins possible.
Acceptance criteria:
• The currywurst machine accepts any coins or banknotes but returns only
coins and works only with EUR currency.
• Function accepts 2 parameters: currywurst_price and eur_inserted
• Function returns a single data structure instructing the currywurst machine
to return the correct amount of coins. You can choose the structure yourself.
• Function works for any positive number.
## 2. A REST API
Now that we have a function that returns the correct amount of coins to save
our colleagues loads of money, we would like to expose this functionality via a
REST API that our currywurst machine can call.
Acceptance criteria:
• The API exposes an endpoint /pay that we can send the amount of inserted
coins to, and it will return the lowest amount of coins possible (use the
solution from 1.).
• You can decide which HTTP method makes sense here.
## 3. A service
To transfer this REST API to other currywurst machines that may run on
different hardware, we want to make this a service that can run on any currywurst
1
machine. The task is to dockerize the application assuming it will run on an
x86-64 machine.
Acceptance criteria:
• The application from step 2. is run inside a docker container and is
reachable from the host machine on localhost:3003/pay
## 4. Events dispatch
Now that we have our new service running and receiving payments, we realize
that we need the history of transactions to control if everything works properly.
Acceptance criteria:
• After the payment transaction is processed by the REST API, but before
returning the result, create and dispatch a new event to notify about the
transaction.
• Choose a persistent storage technology to store the events.
• Start this new service in another container, allowing the REST API to
send events to it.
## Submission
• Please use Python for the implementation
• You are allowed to use 3rd party libraries
• Please submit your solution to the above problems as a zip file and send it
to career@apheris.com
• Please share with us the time it took you to complete the assignment
Thank you for taking the time and happy coding! :)
## How to run it
```
cd apheris
cp .env.dist .env
cd ..
docker-compose build
docker-compose up
docker-compose run web python manage.py test --keepdb
```
you can use http://127.0.0.1:8000/api/v1/pay to test the API