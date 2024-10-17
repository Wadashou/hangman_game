import string
from hangman_base import choose_word, load_words

class HangmanGame:
    def __init__(self):
        self.secret_word = choose_word()
        self.letters_rest = ["_"]*len(self.secret_word)
        self.wrong = 6
        self.kinds = 0
        self.init = "".join(self.letters_rest)
        
        
    def is_word_guessed(self):#ゲームの終了を判定
        for i in self.secret_word:
            if i not in self.letters_rest:
                return False
        return True
    
    def get_guessed_word(self, letters_guessed):#途中経過の生成
        result = "".join(self.letters_rest)
        if letters_guessed in self.secret_word:
            for i, c in enumerate(self.secret_word):
                if c == letters_guessed:
                    self.letters_rest[i] = letters_guessed
                    result = "".join(self.letters_rest)
                    
        return result
    
    def get_available_letters(self, letters_guessed):#残りの使える文字
        all_letters = string.ascii_lowercase
        left_letters = all_letters
        for letter in letters_guessed:
            if letter in self.secret_word:
                left_letters = left_letters.replace(letters_guessed, "")
                return left_letters
            else:
                return left_letters
    
    def count_wrong(self, letters_guessed):#残りの回答数
        for letter in letters_guessed:
            if letter not in self.secret_word:
                return False
            else:
                return True
    
    def count_kinds(self, letters_guessed):#答えの単語が含む文字の種類
        for letter in letters_guessed:
            if letter not in self.secret_word:
                return False
            else:
                return True
            
    def interactivePlay(self):#ゲームの実行
        print("\n""Hagmanゲームを始めます")
        print("\n""答えの単語は{}文字です".format(len(self.secret_word)))
        print("\n",self.init)
        print("\n""あと{}回間違えるとゲームは終了です".format(self.wrong))
        print("\n""残っている文字は : {}".format(string.ascii_lowercase))
        while not self.is_word_guessed():
            letters_guessed = input("文字を入力してください : ").lower()
            
            if not self.count_wrong(letters_guessed):
                self.wrong -= 1
                print("不正解")
            if self.count_kinds(letters_guessed):
                self.kinds += 1
                print("正解")
            print(self.get_guessed_word(letters_guessed))
            print("------------------------") 
            print("\n""あと{}回間違えるとゲーム終了です".format(self.wrong))
            print("残っている文字 : " ,(self.get_available_letters(letters_guessed)))
            if self.wrong == 0:
                print("\n""あなたの負けです。正解は{}でした。".format(self.secret_word))
                break
            if self.is_word_guessed():
                print("正解です: ")
                print("\n",self.secret_word)
                print("\n""----------------------")
                print("\n""あなたの勝ちです")
                print("\n""スコア : {}".format(self.wrong*self.kinds))
                break


#game = HangmanGame()
#game.interactivePlay()


class Hints(HangmanGame):
    def __init__(self):
        super().__init__()
        
        
    def partialMatch(self, letters_guessed):#部分一致の判定
        words_list = load_words()
        results = super().get_guessed_word(letters_guessed)
        for i , s in zip(results, words_list):
            if i != s and i != "_":
                return False
        
        return True
    
    def showCandidates(self, letters_guessed):#解答候補の表示
        results = super().get_guessed_word(letters_guessed)
        results = results.replace("_", "")
        wordlist = set(load_words())
        lists = []
        for word in wordlist:
            if results in word:
                lists.append(word)
        
        return lists
    
    def interactivePlay(self):#ゲームの実行
        print(self.secret_word)
        print("\n""Hagmanゲームを始めます")
        print("\n""答えの単語は{}文字です".format(len(self.secret_word)))
        print("\n",self.init)
        print("\n""あと{}回間違えるとゲームは終了です".format(self.wrong))
        print("\n""残っている文字は : {}".format(string.ascii_lowercase))
        while not self.is_word_guessed():
            letters_guessed = input("文字を入力してください : ").lower()
            #if self.partialMatch(letters_guessed):
            if not self.count_wrong(letters_guessed):
                self.wrong -= 1
                print("不正解")
            if self.count_kinds(letters_guessed):
                self.kinds += 1
                print("正解")
            print(self.get_guessed_word(letters_guessed))
            print("------------------------") 
            print("\n""あと{}回間違えるとゲーム終了です".format(self.wrong))
            print("残っている文字 : " ,(self.get_available_letters(letters_guessed)))
            if len(self.showCandidates(letters_guessed)) <= 20:
                print("\n""ヒント: ここまでの文字が一致する単語は")
                print("\n",self.showCandidates(letters_guessed))
            if self.wrong == 0:
                print("\n""あなたの負けです。正解は{}でした。".format(self.secret_word))
                break
            if self.is_word_guessed():
                print("正解です: ")
                print("\n",self.secret_word)
                print("\n""----------------------")
                print("\n""あなたの勝ちです")
                print("\n""スコア : {}".format(self.wrong*self.kinds))
                break

    
game2 = Hints()
game2.interactivePlay()