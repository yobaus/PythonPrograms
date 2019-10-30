# based on https://www.reddit.com/r/beginnerprojects/comments/1aw0iq/project_turn_based_pokemon_style_game/
# By Pete Baus 10/30/2019
import random
from tkinter import ttk, Toplevel  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk


class Window:
    def __init__(self):
        self.Root = ThemedTk(theme="blue")
        self.Root.config(bg='steel blue3')
        self.Root.title('Monster Fight!!!')
        self.TopFrame = ttk.Frame(self.Root)
        self.BottomFrame = ttk.Frame(self.Root)
        self.TopFrame.pack(side='top', fill='both', padx=60, pady=60)
        self.BottomFrame.pack(side='bottom', fill='both')

        self.StrongAttackButton = ttk.Button(
            self.BottomFrame, text='Strong Attack', command=lambda: self.UseAbility('StrongAttack'))
        self.QuickAttackButton = ttk.Button(
            self.BottomFrame, text='Quick Attack', command=lambda: self.UseAbility('QuickAttack'))
        self.HealButton = ttk.Button(
            self.BottomFrame, text='Heal', command=lambda: self.UseAbility('Heal'))
        self.BlockButton = ttk.Button(
            self.BottomFrame, text='Block', command=lambda: self.UseAbility('Block'))

        self.SumitButton = ttk.Button(
            self.BottomFrame, text='Submit', command=self.NamingMonster)
        self.HelpButtom = ttk.Button(
            self.BottomFrame, text='Help', command=self.HelpWindow)
        self.MonsterNameLable = ttk.Label(self.BottomFrame)
        self.MonsterNameForm = ttk.Entry(self.TopFrame)
        self.MainScreenText = ttk.Label(
            self.TopFrame, text='Please select a move.')
        self.TitleScreen = ttk.Label(
            self.TopFrame, text='Monster Fight!!!', font=("Courier", 44))
        self.TextonScreen = ttk.Label(
            self.TopFrame, text='Please Type your monster name, if you blank a monster name will be randomly picked for you')

    def NamingMonster(self):
        if (self.MonsterNameForm.get()):
            Player.Name = self.MonsterNameForm.get()
        self.TextonScreen.pack_forget()
        self.TitleScreen.pack_forget()
        self.SumitButton.pack_forget()
        self.MonsterNameForm.pack_forget()
        MainWindow.MainBattleScreen()

    def NameScreen(self, Target):
        self.TitleScreen.pack(padx=15, pady=15)
        self.TextonScreen.pack()
        self.SumitButton.pack()
        self.MonsterNameForm.pack()

    def MainBattleScreen(self):
        self.MonsterNameLable.config(text='Press A Button below!')

        self.StrongAttackButton.pack()
        self.QuickAttackButton.pack()
        self.HealButton.pack()
        self.BlockButton.pack()
        self.MainScreenText.pack()
        self.MonsterNameLable.pack(pady=10, padx=10)
        self.HelpButtom.pack(pady=10, padx=10)
        self.MonsterNameLable.config(text='{} Life {} Vs {} Life {}'.format(
            Player.Name, Player.Heath, Computer.Name, Computer.Heath))

    def EndScreen(self, Winner):
        self.StrongAttackButton.pack_forget()
        self.QuickAttackButton.pack_forget()
        self.HealButton.pack_forget()
        self.BlockButton.pack_forget()
        self.MonsterNameLable.pack_forget()
        self.MainScreenText.config(
            text='{} Won the Match!!!!'.format(Winner.Name))

    def UseAbility(self, Move):
        Player.Move = Move
        self.MainScreenText.config(text=(Fight(Computer, Player)))
        self.MonsterNameLable.config(text='{} (Life {}) Vs {} (Life {})'.format(
            Player.Name, Player.Heath, Computer.Name, Computer.Heath))

    def HelpWindow(self):
        try:
            self.HelpSubWindow.destroy()
        except:
            pass
        self.HelpSubWindow = Toplevel(self.Root, bg='steel blue3')
        self.HelpSubWindow.title('Help')
        self.HelpFrame = ttk.Frame(self.HelpSubWindow)
        self.HelpFrame.pack(fill='both')
        self.CloseButton = ttk.Button(self.HelpFrame, text="Close",
                                      command=lambda: self.HelpSubWindow.destroy())
        self.HelpText = ttk.Label(self.HelpFrame, text='Your Monster has Four moves a Strong Attack, a Quick Attack, a Heal, and a Block.\nStrong Attack dose the most damage but is slow, Quick Attack is faster, but dose less damage. \nHeal will heal your monster based on there magic score, Block will incoming damge, but if your \nmonster is to slow it will still get hit!')
        self.MonsterStats = ttk.Label(self.HelpFrame,
                                      text='Your Monsters status are {}'.format(Player))
        self.CloseButton.grid(row=2, column=0, pady=10)
        self.MonsterStats.grid(row=1, column=0, sticky='W', pady=10, padx=20)
        self.HelpText.grid(row=0, column=0, sticky='W', padx=10, pady=20)


class Monster:
    def __init__(self, x=False):
        Namelist = (
            'Doomtree',
            'Aurabody',
            'Metalcreep',
            'Cloudtaur',
            'The Quiet Shrieker',
            'The Grim Shrieker',
            'The Agitated Tumor',
            'The Supreme Corpse Lynx',
            'The Diabolical Butcher Monster',
            'The Ivory Blaze Monkey',
            'Webbeing',
            'Cinderbrute',
            'Glowling',
            'Umbrawraith',
            'The Black Herder',
            'The Dismal Deviation',
            'The Dreary Anomaly',
            'The Glacial Vision Beast',
            'The Barb-Tailed Skeleton Behemoth',
            'The Howling Frost Boar')
        self.Name = x if x else (
            Namelist[random.randint(0, 19)])
        self.Magic = random.randint(1, 25)
        self.speed = random.randint(1, 25)
        self.Attack = random.randint(1, 25)
        self.Defence = random.randint(1, 25)
        self.Heath = random.randint(60, 350)
        self.penalty = 0
        self.Move = 0

    def StrongAttack(self):
        self.penalty = -6
        Damage = (random.randint(9, 15)) + self.Attack
        return ('StrongAttack', Damage)

    def QuickAttack(self):
        self.penalty = 0
        Damage = (random.randint(1, 10)) + self.Attack
        return ('QuickAttack', Damage)

    def Heal(self):
        self.penalty = 0
        Healing = (random.randint(1, 10)) + self.Magic
        return ('Heal', Healing)

    def Block(self):
        self.penalty = 0
        Block = (random.randint(8, 13)) + self.Defence
        return ('Block',  Block)

    def Initiative(self):
        self.penalty = 0
        Initiative = (random.randint(1, 100)) + self.speed + self.penalty
        return Initiative

    def __repr__(self):
        return ('Name {}, Magic {}, Speed {}, Attack {}, Defence {}, Heath {} '.format(self.Name, self.Magic, self.speed, self.Attack, self.Defence, self.Heath))


class AI(Monster):
    def MovePick(self):
        if self.Heath <= 80:
            if random.randint(1, 100) <= 70:
                Num = random.randint(3, 4)
            else:
                Num = random.randint(1, 4)
        else:
            Num = random.randint(1, 2)
        if Num == 1:
            self.penalty = -6
        else:
            self.penalty = 0
        if Num == 1:
            return self.StrongAttack()
        elif Num == 2:
            return self.QuickAttack()
        elif Num == 3:
            return self.Heal()
        elif Num == 4:
            return self.Block()


class PC(Monster):
    def Setup(self):
        PInpute = input(
            'What is your Monter name? Press Enter for a random name.: ')
        MonterName = PInpute if PInpute else self.Name
        self.Name = MonterName

    def MovePick(self):
        Pick = self.Move
        if Pick == 'StrongAttack':
            self.penalty = -6
        else:
            self.penalty = 0
        if Pick == 'StrongAttack':
            return self.StrongAttack()
        elif Pick == 'QuickAttack':
            return self.QuickAttack()
        elif Pick == 'Heal':
            return self.Heal()
        elif Pick == 'Block':
            return self.Block()


def Fight(CPU, PC):
    Move1 = CPU.MovePick()
    Move2 = PC.MovePick()
    Initiative1 = CPU.Initiative()
    Initiative2 = PC.Initiative()

    if Initiative1 > Initiative2:
        if Move1[0] in ('QuickAttack', 'StrongAttack'):
            PC.Heath -= (Move1[1])
        elif Move1[0] == 'Heal':
            CPU.Heath += (Move1[1])

        if Move2[0] in ('QuickAttack', 'StrongAttack'):
            if Move1[0] == 'Block':
                Damage = ((Move2[1]) - (Move1[1])
                          ) if (Move2[1] - Move1[1]) < 0 else 0
                CPU.Heath -= (Damage)
            else:
                CPU.Heath -= (Move2[1])
        elif Move2[0] == 'Heal' and PC.Heath > 0:
            PC.Heath += (Move2[1])
    else:
        if Move2[0] in ('QuickAttack', 'StrongAttack'):
            CPU.Heath -= (Move2[1])
        elif Move2[0] == 'Heal' and PC.Heath > 0:
            PC.Heath += (Move2[1])

        if Move1[0] in ('QuickAttack', 'StrongAttack'):
            if Move2[0] == 'Block':
                Damage = ((Move1[1]) - (Move2[1])
                          ) if ((Move1[1]) - (Move2[1])) > 0 else 0
                CPU.Heath -= (Damage)
            else:
                PC.Heath -= (Move1[1])
        elif Move1[0] == 'Heal':
            CPU.Heath += (Move1[1])
    if Computer.Heath <= 0:
        MainWindow.EndScreen(Player)
    elif Computer.Heath <= 0:
        MainWindow.EndScreen(Computer)
    else:
        return ('{} used {} moved and heath is now {}. \n {} used {} and heath is now {}. '.format(
            CPU.Name, Move1, CPU.Heath, PC.Name, Move2, PC.Heath))


Computer = AI()
Player = PC()
MainWindow = Window()
MainWindow.NameScreen(Player)
MainWindow.Root.mainloop()
