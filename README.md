# Scanner
scanner de port en python (socket)
Ce projet est un script Python permettant de scanner les ports ouverts d'un hôte cible, et d'identifier les services associés à ces ports. Il peut être utilisé pour effectuer des tests de sécurité ou pour surveiller la disponibilité des services sur un réseau.
Fonctionnalités principales :

    Scan de ports spécifiques ou de plages de ports : Le script permet de scanner des ports uniques, des plages de ports ou tous les ports possibles (de 1 à 65535).

    Détection des services : Si activé, le script tente de détecter les services associés aux ports ouverts (par exemple, HTTP pour le port 80).

    Prise en charge de plusieurs hôtes : Il est possible de scanner plusieurs hôtes à la fois.

    Options de détection du système d'exploitation (à implémenter) : Bien que non entièrement fonctionnelle, le script prévoit une option pour détecter l'OS de l'hôte cible à l’aide de nmap.

Commandes :

    -t (ou --target) : Spécifie l'hôte cible à scanner.

    -p (ou --port) : Détermine un port spécifique ou une plage de ports à scanner. Exemple : -p 80, -p 100-200.

    -s (ou --service) : Active la détection des services sur les ports ouverts.

    -o (ou --OS) : Active la détection de l'OS de l'hôte cible (fonction à implémenter).

    -h (ou --help) : Affiche l'aide du script.
