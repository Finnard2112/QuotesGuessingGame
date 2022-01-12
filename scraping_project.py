import bs4
import requests
from random import choice


url = "http://quotes.toscrape.com"
big_list = []
current_page = 1
q = True
while q:
    response = requests.get(url + f"/page/{current_page}/")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    q = soup.find_all(class_="quote")
    for x in q:
        text = x.find(class_="text").get_text()
        author = x.find(class_="author").get_text()
        href = x.find("a")["href"]
        big_list.append([text, author, href])
    current_page += 1


def main():
    display = choice(big_list)
    print(display[0])
    response = requests.get(url + display[2])
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    count = 4
    while count <= 4 and count > 0:
        answer = input(f"Who said this quote? {count} guesses remaining")
        if answer == display[1]:
            play_again = input("Congrats, play again? y/n")
            if play_again == "y":
                main()
            exit()
        count -= 1
        if count == 3:
            print(
                "Hint: Born " +
                soup.find(
                    class_="author-born-date").get_text() +
                " " +
                soup.find(
                    class_="author-born-location").get_text())
        if count == 2:
            print("Hint: First letter of first name is " + display[1][0])
        if count == 1:
            x = display[1].split()
            print("Hint: First letter of last name is " + x[-1][0])
    print(display[1])
    play_again = input("No more guesses, play again? y/n")
    if play_again == "y":
        main()
    exit()


main()
