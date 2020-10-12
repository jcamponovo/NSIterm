#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Permet de tout executer au lancement du notebook + conserver le notebook actif pendant 2h
from IPython.display import Javascript
from masquer import *
Javascript("""
function repeter(){
IPython.notebook.kernel.execute("a=1");
}
// execute a = 1 en python toutes les 8 minutes pendant 2h
let timerId = setInterval(() => repeter(), 4800);
setTimeout(() => { clearInterval(timerId); alert('fin de cession'); }, 7200000);

// Supprimer la taille limite pour la sortie d'une cellule
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
};
IPython.notebook.kernel.execute("url = '" + window.location + "'");

// Exécuter toutes les cellule du notebook
    require(
        ['base/js/namespace', 'jquery'], 
        function(jupyter, $) {
            
                
                jupyter.actions.call('jupyter-notebook:run-all-cells-below');
                jupyter.actions.call('jupyter-notebook:save-notebook');
                Jupyter.actions.call('jupyter-notebook:hide-header')

        }
    );""")


# In[3]:


HTML("""<style>
h1 {
  font-family: 'Permanent Marker', cursive;
  text-align: center;
  color: red;
  
}
ol {
  list-style-position: inside;
  margin-left: 1em;
  list-style-position: outside;
}
h2 {
  font-family: 'Permanent Marker', cursive;
  color: blue;
}
</style>""")


# # <span style="color:red;"><center>TD_00_1 : Rappels de première</center></span>

# 1. Ecrire une fonction **binaire** qui prend comme argument un int et qui renvoie une chaine de caractère représentant le binaire correspondant. Pour rappel, la conversion se fait par divisions successives par deux.
# Par exemple: binaire(2) doit renvoyer "10" et binaire(7) "111". Votre fonction devra être correctement commentée et documentée.

# In[4]:


# Question 1.


# 2. Construire par compréhension une liste contenant tous les entiers impairs compris entre 0 et 10.
# 3. Stocker cette liste dans une variable $l$

# In[14]:


# Questions 2 et 3
numbers = range (11)
for number in numbers :
    if number % 2 != 0 :
        print ( number )

L = number


# 4. Associer dans un dictionnaire les valeurs n et 3n+2 pour $0\le n \le 50$

# In[15]:


# Question 4
n = range (0, 51)
dictionnaire = {
    "n": "3n+2"
}


# 5. Ecrire une fonction **tri_insertion** qui prend comme argument une liste de floats et qui renvoie la liste de floats triés dans l'ordre croissant par un algorithme de tri insertion. Vous pouvez regarder la vidéo ci-dessous pour vous rappeler l'algorithme.

# In[7]:


from IPython.display import HTML,IFrame
HTML("""<iframe width="640" height="480" src="https://www.youtube.com/embed/ROalU379l3U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""")


# In[8]:


# Question 5
from random import *
def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
            tab[j + 1] = tab[j]
            j -=1
        tab[j + 1] = k


# 6. Etudiez et commentez la fonction mystere suivante.

# In[17]:


# Question 6
from random import *
entree = [randint(0,1000) for i in range(20)] # prend 20 nombres entre 0 et 999 au hasard

def mystere(liste):
    m = liste[0]
    for val in liste:
        if val > m: # si la valuer est strictement plus grand que m
            m = val # m la plus grande valeur
    return m 

print(entree)
mystere(entree)


# 7. Modifiez la fonction mystere ci-dessous pour qu'elle renvoie aussi l'indice correspondant à m

# In[18]:


# Question 7
entree = [randint(0,1000) for i in range(20)]

def mystere(liste):
    m = liste[0]
    for val in liste:
        if val > m:
            m = val
    return m

print(entree)
mystere(entree)


# 8. Etudiez la fonction mystere2 suivante. Documentez là et commentez là.

# In[19]:


# Question 8
entree = sorted([randint(0,1000) for i in range(100)])


def mystere2(liste,val): 
    l = liste[:]
    while l:
        n = len(l)
        if val < l[n//2]:
            l = l[:n//2]
        elif val == l[n//2]:
            return True
        else:
            l = l[n//2+1:]
    return False
            

print(entree)    
mystere2(entree,300)

