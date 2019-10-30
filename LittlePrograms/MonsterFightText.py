# based on https://www.reddit.com/r/beginnerprojects/comments/1aw0iq/project_turn_based_pokemon_style_game/
# By Pete Baus 10/30/2019
import random
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
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
            self.BottomFrame, text='Strong Attack', command=lambda: UseAbility('StrongAttack'))
        self.QuickAttackButton = ttk.Button(
            self.BottomFrame, text='Quick Attack', command=lambda: UseAbility('QuickAttack'))
        self.HealButton = ttk.Button(
            self.BottomFrame, text='Heal', command=lambda: UseAbility('Heal'))
        self.BlockButton = ttk.Button(
            self.BottomFrame, text='Block', command=lambda: UseAbility('Block'))

        self.SumitButton = ttk.Button(
            self.BottomFrame, text='Submit', command=self.NamingMonster)
        self.MonsterNameLable = ttk.Label(self.BottomFrame)
        self.MonsterNameForm = ttk.Entry(self.TopFrame)
        self.TextonScreen = ttk.Label(
            self.TopFrame, text='Please Type your monster name, if you blank a monster name will be randomly picked for you')

    def NamingMonster(self):
        if (self.MonsterNameForm.get()):
            Player.Name = self.MonsterNameForm.get()
        print(Player.Name)
        self.TextonScreen.pack_forget()
        self.SumitButton.pack_forget()
        self.MonsterNameForm.pack_forget()

    def NameScreen(self, Target):
        self.TextonScreen.pack()
        self.SumitButton.pack()
        self.MonsterNameForm.pack()

    def MainBattleScreen(self):
        self.StrongAttackButton.pack()
        self.QuickAttackButton.pack()
        self.HealButton.pack()
        self.BlockButton.pack()
        self.MonsterNameLable.pack()

    def UseAbility(self, Move):
        Player.Move = Move


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
            Namelist[random.randint(0, len(Namelist))])
        self.Magic = random.randint(1, 25)
        self.speed = random.randint(1, 25)
        self.Attack = random.randint(1, 25)
        self.Defence = random.randint(1, 25)
        self.Heath = random.randint(60, 350)
        self.penalty = 0

    def StrongAtack(self):
        self.penalty = -6
        Damage = (random.randint(9, 15)) + self.Attack
        return ('StrongAtack', Damage)

    def FastAtack(self):
        self.penalty = 0
        Damage = (random.randint(1, 10)) + self.Attack
        return ('FastAtack', Damage)

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
        Num = random.randint(1, 4)
        if Num == 1:
            self.penalty = -6
        else:
            self.penalty = 0
        if Num == 1:
            return self.StrongAtack()
        elif Num == 2:
            return self.FastAtack()
        elif Num == 3:
            return self.Heal()
        elif Num == 4:
            return self.Block()


class PC(Monster):
    def __intit__(self):
        Monster.__init__(self)
        self.Move = 0

    def Setup(self):
        PInpute = input(
            'What is your Monter name? Press Enter for a random name.: ')
        MonterName = PInpute if PInpute else self.Name
        self.Name = MonterName

    def MovePick(self):
        Pick = self.Move
        if Pick == 'StrongAtack':
            self.penalty = -6
        else:
            self.penalty = 0
        if Pick == 'StrongAtack':
            return self.StrongAtack()
        elif Pick == 'FastAtack':
            return self.FastAtack()
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
        if Move1[0] in ('FastAtack', 'StrongAtack'):
            PC.Heath -= (Move1[1])
        elif Move1[0] == 'Heal':
            CPU.Heath += (Move1[1])

        if Move2[0] in ('FastAtack', 'StrongAtack'):
            if Move1[0] == 'Block':
                Damage = ((Move2[1]) - (Move1[1])
                          ) if (Move2[1] - Move1[1]) < 0 else 0
                CPU.Heath -= (Damage)
            else:
                CPU.Heath -= (Move2[1])
        elif Move2[0] == 'Heal' and PC.Heath > 0:
            PC.Heath += (Move2[1])
    else:
        if Move2[0] in ('FastAtack', 'StrongAtack'):
            CPU.Heath -= (Move2[1])
        elif Move2[0] == 'Heal' and PC.Heath > 0:
            PC.Heath += (Move2[1])

        if Move1[0] in ('FastAtack', 'StrongAtack'):
            if Move2[0] == 'Block':
                Damage = ((Move1[1]) - (Move2[1])
                          ) if ((Move1[1]) - (Move2[1])) > 0 else 0
                CPU.Heath -= (Damage)
            else:
                PC.Heath -= (Move1[1])
        elif Move1[0] == 'Heal':
            CPU.Heath += (Move1[1])
    print('{} used {} moved and heath is now {}. \n {} used {} and heath is now {}. '.format(
        CPU.Name, Move1, CPU.Heath, PC.Name, Move2, PC.Heath))


Computer = AI()
Player = PC()
Player.Setup()

loop = True

while loop:
    Player.Move = input('Whats your move: ')
    Fight(Computer, Player)
    if Computer.Heath <= 0:
        print('{} Wins!'.format(Player.Name))
        break
    elif Player.Heath <= 0:
        print('{} Wins!'.format(Computer.Name))
        break
