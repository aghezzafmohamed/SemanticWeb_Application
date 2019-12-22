"""
Created on Fri Dec 20 19:52:04 2019

@author: AGHEZZAF Mohamed
@email:  aghe.mohamed@gmail.com
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from nltk.corpus import wordnet
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os
lemmatizer = WordNetLemmatizer()

class Ui_Form(object):
    def ParcourirCorpus(self):
        self.plainTextEdit.setPlainText("")
        request=self.lineEdit.text()
        if (request == ""):
            self.plainTextEdit.setPlainText("Voulez entrez d'abord le chemin des fichiers")
        else:
            self.groupBox.setTitle("Le text")
            for element in os.listdir(request):
                if element.endswith('.txt'):
                    pat=request+'\\'+element
                    fichier = open(pat, "r")
                    self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'<br><br>'+str(fichier.read())+'</span><br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999">')
            self.pushButton_9.setEnabled(True)

    def RepresentationDuCorpus(self):
        self.plainTextEdit.setPlainText("")
        request=self.lineEdit.text()
        self.groupBox.setTitle("Résultat tokenisation")
        for element in os.listdir(request):
            if element.endswith('.txt'):
                pat=request+'\\'+element
                fichier = open(pat, "r")
                self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'</span><br>')
                word_list = nltk.word_tokenize(fichier.read())
                for w in word_list:
                    self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+w+'</span>')
                self.plainTextEdit.appendHtml('<br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999"><br>')
        self.pushButton_10.setEnabled(True)
        
    def Elimination(self):
        self.plainTextEdit.setPlainText("")
        request=self.lineEdit.text()
        self.groupBox.setTitle("Résultat tokens nettoyés")
        for element in os.listdir(request):
            if element.endswith('.txt'):
                pat=request+'\\'+element
                fichier = open(pat, "r")
                self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'</span><br>')
                word_list = nltk.word_tokenize(fichier.read())
                stop_words = set(stopwords.words('english'))
                filtered_sentence = [w for w in word_list if not w in stop_words]
                filtered_sentence = []
                for w in word_list:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                chaine=" ".join(filtered_sentence)
                chaine=chaine.lower()
                tokens = nltk.word_tokenize(chaine)
    
                tokens = [word.lower() for word in tokens if word.isalpha()]
                for w in tokens:
                    self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+w+'</span>')
                self.plainTextEdit.appendHtml('<br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999"><br>')
        self.pushButton_11.setEnabled(True)
    
    def CalculOccurrence(self):
        self.plainTextEdit.setPlainText("")
        request=self.lineEdit.text()
        self.groupBox.setTitle("Résultat occurrences")
        for element in os.listdir(request):
            if element.endswith('.txt'):
                pat=request+'\\'+element
                fichier = open(pat, "r")
                self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'</span><br>')
                word_list = nltk.word_tokenize(fichier.read())
                stop_words = set(stopwords.words('english'))
                filtered_sentence = [w for w in word_list if not w in stop_words]
                filtered_sentence = []
    
                for w in word_list:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                chaine=" ".join(filtered_sentence)
                chaine=chaine.lower()
                tokens = nltk.word_tokenize(chaine)
    
                tokens = [word.lower() for word in tokens if word.isalpha()]
                # deux dictionnaires vide
                d = {}
                ch = " ".join(tokens)
                token_words = word_tokenize(ch)
                token_words
                stem_sentence = []
                porter = PorterStemmer()
                for word in token_words:
                    stem_sentence.append(porter.stem(word))
                    stem_sentence.append(" ")
                ch = " ".join(stem_sentence)
                list = []
                list = ch.split(" ")
                for l in list:
                    if l != "":
                        d[l] = list.count(l)
                        self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+l + "   >>>>>>>>>>    " + str(d[l]) +'</span>')
            self.plainTextEdit.appendHtml('<br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999"><br>')
        self.pushButton_12.setEnabled(True)

    def Lemmatisation(self):
        self.plainTextEdit.setPlainText("")
        request = self.lineEdit.text()
        self.groupBox.setTitle("Résultat lemmatisation")
        for element in os.listdir(request):
            if element.endswith('.txt'):
                pat = request + '\\' + element
                fichier = open(pat, "r")
                self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'</span><br>')
                word_list = nltk.word_tokenize(fichier.read())
                stop_words = set(stopwords.words('english'))
                filtered_sentence = [w for w in word_list if not w in stop_words]
                filtered_sentence = []
    
                for w in word_list:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                chaine = " ".join(filtered_sentence)
                chaine = chaine.lower()
                tokens = nltk.word_tokenize(chaine)
    
                tokens = [word.lower() for word in tokens if word.isalpha()]
                # deux dictionnaires vide
                d = {}
                ch = " ".join(tokens)
                token_words = word_tokenize(ch)
                token_words
                stem_sentence = []
                porter = PorterStemmer()
                for word in token_words:
                    stem_sentence.append(porter.stem(word))
                    stem_sentence.append(" ")
                ch = " ".join(stem_sentence)
                list = []
                list = ch.split(" ")
                for l in list:
                    if l != "":
                        s =lemmatizer.lemmatize(l)
                        d[s] = list.count(l)
                        self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+s +'</span>')
            self.plainTextEdit.appendHtml('<br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999"><br>')
        self.pushButton_13.setEnabled(True)

    def Synset(self):
        self.plainTextEdit.setPlainText("")
        request = self.lineEdit.text()
        self.groupBox.setTitle("Résultat synsets")
        for element in os.listdir(request):
            if element.endswith('.txt'):
                pat = request + '\\' + element
                fichier = open(pat, "r")
                self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+element+'</span><br>')
                word_list = nltk.word_tokenize(fichier.read())
                stop_words = set(stopwords.words('english'))
                filtered_sentence = [w for w in word_list if not w in stop_words]
                filtered_sentence = []
    
                for w in word_list:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                chaine = " ".join(filtered_sentence)
                chaine = chaine.lower()
                tokens = nltk.word_tokenize(chaine)
    
                tokens = [word.lower() for word in tokens if word.isalpha()]
                # deux dictionnaires vide
                d = {}
                ch = " ".join(tokens)
                token_words = word_tokenize(ch)
                token_words
                stem_sentence = []
                porter = PorterStemmer()
                for word in token_words:
                    stem_sentence.append(porter.stem(word))
                    stem_sentence.append(" ")
                ch = " ".join(stem_sentence)
                list = []
                list = ch.split(" ")
                for l in list:
                    if l != "":
                        s =lemmatizer.lemmatize(l)
                        d[s] = list.count(l)
    
                for key, value in d.items():
                    synonyms = []
                    for syn in wordnet.synsets(key):
                        for l in syn.lemmas():
                            synonyms.append(l.name())
                    if len(synonyms) == 0:
                        self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">Synset de '+key+" >>>>>> "+key+'</span>')
                    else:
                        self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">Synset de '+key+" >>>>>> "+synonyms[0]+'</span>')
            self.plainTextEdit.appendHtml('<br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#3d3d3d">_______________________________________________</font></span> <span style=" font-size: 11px; color: #999"><br>')
        self.lineEdit_2.setEnabled(True)
        self.pushButton_32.setEnabled(True)
        self.lineEdit_2.setText( "Mot à cherché")

    def RechercheSemantique(self):
        self.plainTextEdit.setPlainText("")
        request = self.lineEdit.text()
        self.groupBox.setTitle("Résultats de recherche sémantique")
        req = self.lineEdit_2.text()
        if(req==""):
            self.plainTextEdit.setPlainText("Voulez entrez d'abord la requête à chercher")
        else:
            synonyms = []
            for syn in wordnet.synsets(req):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            if len(synonyms) == 0:
                req = req
            else:
                req=synonyms[0]
            self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">Les documents sémantiques par rapport au terme "'+req+'" sont: </span><br>')
            for element in os.listdir(request):
                if element.endswith('.txt'):
                    pat=request+'\\'+element
                    fichier = open(pat, "r")
                    stop_words = set(stopwords.words('english'))
    
                    word_tokens = nltk.word_tokenize(fichier.read())
    
                    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    
                    filtered_sentence = []
    
                    for w in word_tokens:
                        if w not in stop_words:
                            filtered_sentence.append(w)
                    chaine=" ".join(filtered_sentence)
                    chaine=chaine.lower()
                    tokens = nltk.word_tokenize(chaine)
                    tokens = [word.lower() for word in tokens if word.isalpha()]
                    # deux dictionnaires vide
                    d = {}
                    d2={}
                    ch = " ".join(tokens)
                    token_words = word_tokenize(ch)
                    stem_sentence = []
                    porter = PorterStemmer()
                    for word in token_words:
                        stem_sentence.append(porter.stem(word))
                        stem_sentence.append(" ")
                    ch=" ".join(stem_sentence)
                    list = []
                    list=ch.split(" ")
                    for l in list:
                        if l!="":
                            s = lemmatizer.lemmatize(l)
                            d[s]=list.count(l)
    
                    for key, value in d.items():
                        synonyms = []
                        for syn in wordnet.synsets(key):
                            for l in syn.lemmas():
                                synonyms.append(l.name())
                        if len(synonyms)==0:
                            synonyms=key
                            d2[synonyms] = value
                        else:
                            d2[synonyms[0]] = value
                    for key, value in d2.items():
                        if req==key:
                            self.plainTextEdit.appendHtml('<span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">Le terme "'+key+'" trouvé dans le document "'+element+'" avec une occurence: '+str(value)+' </span><br>')
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(874, 527)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        Form.setToolTip("")
        Form.setStatusTip("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-size:20px;\n"
"font-family:sans-serif;\n"
"}\n"
"#label{\n"
"\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_4{\n"
"background:url(:/images/us.png);\n"
"height: 5px\n"
"}\n"
"#label_2{\n"
"background:#13386d;\n"
"height: 5px\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"#frame_2{\n"
"background:url(:/images/us.png);\n"
"}\n"
"#frame1{\n"
"background:#3d3d3d;\n"
"}\n"
"#pushButton_8{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_8:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_9{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_9:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_10{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_10:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_11{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_11:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_12{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_12:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_13{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_13:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"#pushButton_32{\n"
"background:rgb(80, 80, 80);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"\n"
"#pushButton_32:hover{\n"
"background:rgb(111, 111, 111);\n"
"font-size:16px;\n"
"color:#fff;\n"
"}\n"
"QLineEdit\n"
"{\n"
" border: 0;\n"
" border-bottom: 2px solid #f8f8f8;\n"
" width: 100%;\n"
" font-size:15px;\n"
" text-align: center;\n"
" background: transparent;\n"
" color: #fff;\n"
"}\n"
"#groupBox\n"
"{\n"
" border-bottom: 1px solid #f8f8f8;\n"
" width: 100%;\n"
" font-size:12px;\n"
" text-align: center;\n"
" border-align: center;\n"
" background: transparent;\n"
" color: #fff;\n"
"}\n"
"#groupBox_2\n"
"{\n"
" border-bottom: 1px solid #f8f8f8;\n"
" width: 100%;\n"
" font-size:12px;\n"
" text-align: center;\n"
" border-align: center;\n"
" background: transparent;\n"
" color: #fff;\n"
"}\n"
"#groupBox_3\n"
"{\n"
" border-bottom: 1px solid #f8f8f8;\n"
" width: 100%;\n"
" font-size:12px;\n"
" text-align: center;\n"
" border-align: center;\n"
" background: transparent;\n"
" color: #fff;\n"
"}\n"
"#groupBox_4\n"
"{\n"
" border-bottom: 1px solid #f8f8f8;\n"
" width: 100%;\n"
" font-size:12px;\n"
" text-align: center;\n"
" border-align: center;\n"
" background: transparent;\n"
" color: #fff;\n"
"}\n"
"#plainTextEdit{\n"
"  width: 100%;\n"
"  height: 150px;\n"
"  padding: 2px 4px;\n"
"  box-sizing: border-box;\n"
"  border: 0.2px solid #ccc;\n"
"  border-radius: 0.5px;\n"
"  background-color: #f8f8f8;\n"
"  resize: none;\n"
"overflow:hidden;\n"
"}\n"
".scroll::-webkit-scrollbar {\n"
"   display: none;\n"
" }")
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame1 = QtWidgets.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 881, 531))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.frame1.setFont(font)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.lineEdit = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 571, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 21, 21))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setTabletTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAccessibleDescription("")
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_3.setShortcut("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 480, 21, 31))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setTabletTracking(False)
        self.pushButton_5.setAcceptDrops(False)
        self.pushButton_5.setAccessibleDescription("")
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/C:/Users/ASUS/Desktop/qt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_5.setShortcut("")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 480, 31, 31))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setTabletTracking(False)
        self.pushButton_6.setAcceptDrops(False)
        self.pushButton_6.setAccessibleDescription("")
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_6.setShortcut("")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 10, 21, 21))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setTabletTracking(False)
        self.pushButton_7.setAcceptDrops(False)
        self.pushButton_7.setAccessibleDescription("")
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_7.setShortcut("")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setAutoRepeat(False)
        self.pushButton_7.setAutoExclusive(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox = QtWidgets.QGroupBox(self.frame1)
        self.groupBox.setGeometry(QtCore.QRect(20, 120, 571, 391))
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 551, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame1)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 30, 231, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 70, 211, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 120, 211, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 170, 211, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 220, 211, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 270, 211, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame1)
        self.groupBox_4.setGeometry(QtCore.QRect(620, 380, 231, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_32.setEnabled(False)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 30, 211, 31))
        self.pushButton_32.setObjectName("pushButton_32")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 571, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(630, 490, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox.raise_()
        self.lineEdit.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.groupBox_2.raise_()
        self.groupBox_4.raise_()
        self.pushButton_8.clicked.connect(self.ParcourirCorpus)
        self.pushButton_9.clicked.connect(self.RepresentationDuCorpus)
        self.pushButton_10.clicked.connect(self.Elimination)
        self.pushButton_11.clicked.connect(self.CalculOccurrence)
        self.pushButton_12.clicked.connect(self.Lemmatisation)
        self.pushButton_13.clicked.connect(self.Synset)
        self.pushButton_32.clicked.connect(self.RechercheSemantique)
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "Chemin fichier/corpus"))
        self.groupBox.setTitle(_translate("Form", "Affichage"))
        self.groupBox_2.setTitle(_translate("Form", "Recherche d’information"))
        self.pushButton_8.setText(_translate("Form", "Parcourir Corpus"))
        self.pushButton_9.setText(_translate("Form", "Représentation du corpus"))
        self.pushButton_10.setText(_translate("Form", "Elimination"))
        self.pushButton_11.setText(_translate("Form", "Calcul d’occurrence"))
        self.pushButton_12.setText(_translate("Form", "Lemmatisation"))
        self.pushButton_13.setText(_translate("Form", "Les synset"))
        self.groupBox_4.setTitle(_translate("Form", "Recherche sémantique"))
        self.pushButton_32.setText(_translate("Form", "Recherche sémantique"))
        self.label.setText(_translate("Form", "By : AGHEZZAF MOHAMED"))
