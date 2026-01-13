#!/usr/bin/python3
"""
checkbook.py

Ce script simule un carnet de chèques (checkbook) simple.
Il permet à un utilisateur de :
- déposer de l'argent
- retirer de l'argent
- consulter le solde
via une interface en ligne de commande.
"""

class Checkbook:
    """
    Classe représentant un carnet de chèques.
    Elle gère un solde et des opérations bancaires de base.
    """

    def __init__(self):
        """
        Initialise un nouveau carnet de chèques avec un solde à 0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Paramètre:
            amount (float): montant à ajouter au solde
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte si le solde est suffisant.

        Paramètre:
            amount (float): montant à retirer
        """
        if amount > self.balance:
            # Cas où le solde est insuffisant
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale du programme.
    Elle gère l'interaction avec l'utilisateur et les commandes.
    """
    cb = Checkbook()

    # Boucle principale du programme
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            # Quitte le programme
            break

        elif action.lower() == 'deposit':
            # Dépôt d'argent
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            # Retrait d'argent
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            # Affichage du solde
            cb.get_balance()

        else:
            # Commande inconnue
            print("Invalid command. Please try again.")


# Point d’entrée du script
if __name__ == "__main__":
    main()
