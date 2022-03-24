# -*- coding: utf-8 -*-
"""
Contains functions that are not online APIs.
"""
import random


def magicmirror():
    """ magicmirror by meklin for qwerty

    :return: A random answer.
    :rtype: str
    """
    answers = [
                'My Queen, you are the fairest here so true. But Qwerty is a thousand times more lovely, fair and beautiful than you.', 'Qwerty still lives, fairest in the land. \'Tis the heart of a pig you hold in your hand. ', 'Over the seven jewelled hills, beyond the seventh fall, in the cottage of the Seven Dwarfs, dwells Qwerty, fairest one of all.', 'Lips red as the rose, hair black as ebony, skin white as snow.', 'Famed is thy beauty, Majesty. But hold, a lovely maid I see. Rags cannot hide her gentle grace. Alas, Qwerty is more fair than thee.', 'What wouldst thou know, my Queen?', 'Why, Qwerty is the fairest.'
    ]
    return random.choice(answers)

def tarot_cards():
    """ tarot cards by meklin of reddit9k

    :return: A random answer.
    :rtype: str
    """
    answers = [
                'Fool 😄', 'Magician 🪄', 'High Priestess 👄', 'Empress 👑',
                'Emperor 🧔', 'Heirophant ⚚', 'Lovers 💑', 'Chariot 🐎',
                'Strength 💪', 'Hermit 🥸', 'Wheel of Fortune 🎡', 'Justice ⚖',
                'Hanged Man 🪜', 'Death', 'Temperance 😇',
                'Devil 😈', 'Tower 🗼', 'Star ⭐', 'Moon 🌙',
                'Sun 🌅', 'Judgement 🎺', 'World 🌎',
                'Ace of Wands 🪄', 'Two of Wands 🪄', 'Three of Wands 🪄',
                'Four of Wands 🪄', 'Five of Wands 🪄', 'Six of Wands 🪄',
                'Seven of Wands 🪄', 'Eight of Wands 🪄', 'Nine of Wands 🪄',
                'Ten of Wands 🪄', '♙ Page of Wands 🪄', '♘ Knight of Wands 🪄',
                '♕ Queen of Wands 🪄', '♔ King of Wands 🪄', 'Ace of Pentacles ✪',
                'Two of Pentacles ✪', 'Three of Pentacles ✪', 'Four of Pentacles ✪',
                'Five of Pentacles ✪', 'Six of Pentacles ✪', 'Seven of Pentacles ✪',
                'Eight of Pentacles ✪', 'Nine of Pentacles ✪', 'Ten of Pentacles ✪',
                '♙ Page of Pentacles ✪', '♘ Knight of Pentacles ✪', '♕ Queen of Pentacles ✪',
                '♔ King of Pentacles ✪', 'Ace of Cups 🏆', 'Two of Cups 🏆',
                'Three of Cups 🏆', 'Four of Cups 🏆', 'Five of Cups 🏆',
                'Six of Cups 🏆', 'Seven of Cups 🏆', 'Eight of Cups 🏆',
                'Nine of Cups 🏆', 'Ten of Cups 🏆', '♙ Page of Cups 🏆',
                'Knight of Cups 🏆', '♕ Queen of Cups 🏆', '♔ King of Cups 🏆',
                '🕊 Ace of Swords 🗡', 'Two of Swords 🗡', 'Three of Swords 🗡',
                'Four of Swords 🗡', 'Five of Swords 🗡', 'Six of Swords 🗡',
                'Seven of Swords 🗡', 'Eight of Swords 🗡', 'Nine of Swords 🗡',
                'Ten of Swords 🗡', '♙ Page of Swords 🗡', '♘ Knight of Swords 🗡',
                '♕ Queen of Swords 🗡', '♔ King of Swords 🗡'

    ]
    return random.choice(answers)


def eight_ball():
    """ Magic eight ball.

    :return: A random answer.
    :rtype: str
    """
    answers = [
                'It is certain', 'It is decidedly so', 'without a doubt', 'Yes definitely',
                'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
                'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
                'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
                'Very doubtful'
    ]
    return random.choice(answers)
    
    
def hitler_quote():

    answers = [
                'The leader of genius must have the ability to make different opponents appear as if they belonged to one category.\n― Adolf Hitler',
                'Humanitarianism is the expression of stupidity and cowardice.\n― Adolf Hitler',
                'He who would live must fight. He who doesn\'t wish to fight in this world, where permanent struggle is the law of life, has not the right to exist.\n― Adolf Hitler, Mein Kampf',
                'Yes definitely', 'The great strength of the totalitarian state is that it forces those who fear it to imitate it.\n― Adolf Hitler',
                'Kill, Destroy, Sack, Tell lie; how much you want after victory nobody asks why?\n--uncited source\n― Adolf Hitler',
                'As in everything, nature is the best instructor.\n― Adolf Hitler',
                'The very first essential for success is a perpetually constant and regular employment of violence.\n― Adolf Hitler',
                'The state must declare the child to be the most precious treasure of the people. As long as the government is perceived as working for the benefit of the children, the people will happily endure almost any curtailment of liberty and almost any deprivation.\n― Adolf Hitler',
                'If freedom is short of weapons, we must compensate with willpower.\n― Adolf Hitler',
                'The only preventative measure one can take is to live irregularly.\n― Adolf Hitler, Mein Kampf',
                'Instruction in world history in the so-called high schools is even today in a very sorry condition. Few teachers understand that the study of history can never be to learn historical dates and events by heart and recite them by rote; that what matters is not whether the child knows exactly when this battle or that was fought, when a general was born, or even when a monarch (usually a very insignificant one) came into the crown of his forefathers. No, by the living God, this is very unimportant. To \'learn\' history means to seek and find the forces which are the causes leading to those effects which we subsequently perceive as historical events.\n― Adolf Hitler, Mein Kampf',
                'The scream of the twelve-inch shrapnel is more penetrating than the hiss from a thousand Jewish newspaper vipers. Therefore let them go on with their hissing.\n― Adolf Hitler',
                'The art of reading and studying consists in remembering the essentials and forgetting what is not essential.\n― Adolf Hitler, Mein Kampf',
                'The victor will never be asked if he told the truth. \n― Adolf Hitler, Hitler\'s Letters and Notes',
                'The receptivity of the masses is very limited, their intelligence is small, but their power of forgetting is enormous. In consequence of these facts, all effective propaganda must be limited to a very few points and must harp on these in slogans until the last member of the public understands what you want him to understand by your slogan.\n― Adolf Hitler',
                'Words build bridges into unexplored regions.\n― Adolf Hitler',
                'To conquer a nation, first disarm its citizens.\n― Adolf Hitler',
                'He alone, who owns the youth, gains the future.\n― Adolf Hitler',
                'I use emotion for the many and reserve reason for the few.\n― Adolf Hitler'
                'Reading is not an end to itself, but a means to an end.\n― Adolf Hitler, Mein Kampf'
                'The stronger must dominate and not mate with the weaker, which would signify the sacrifice of its own higher nature. Only the born weakling can look upon this principle as cruel, and if he does so it is merely because he is of a feebler nature and narrower mind; for if such a law did not direct the process of evolution then the higher development of organic life would not be conceivable at all.\n― Adolf Hitler'
                'Only the Jew knew that by an able and persistent use of propaganda heaven itself can be presented to the people as if it were hell and, vice versa, the most miserable kind of life can be presented as if it were paradise. The Jew knew this and acted accordingly. But the German, or rather his Government, did not have the slightest suspicion of it. During the War the heaviest of penalties had to be paid for that ignorance.\n-- Mein Kampf, Chapter 10\n― Adolf Hitler, Mein Kampf'
                'The man who has no sense of history, is like a man who has no ears or eyes\n― Adolf Hitler'
                'When diplomacy ends, War begins.\n― Adolf Hitler'
                'Think Thousand times before taking a decision But - After taking decison never turn back even if you get Thousand difficulties!!\n― Adolf Hitler'
                'Anyone can deal with victory. Only the mighty can bear defeat.\n― Adolf Hitler'
                'And I can fight only for something that I love, love only what I respect, and respect only what I at least know.\n― Adolf Hitler'
                'if you want to shine like sun first you have to burn like it.\n― Adolf Hitler'
                'Do not compare yourself to others. If you do so, you are insulting yourself.\n― Adolf Hitler'
                'If you win, you need not have to explain...If you lose, you should not be there to explain!\n― Adolf Hitler'
                ]
    return random.choice(answers)


def flip_coin():
    """ Flip a coin.

    :return: Heads or tails.
    :rtype: str
    """
    coin = ['heads', 'tails']
    return random.choice(coin)


def roll_dice():
    """ Roll a 6 sided dice.

    :return: A number between 1 and 6.
    :rtype: str
    """
    numbers = ['1', '2', '3', '4', '5', '6']
    return random.choice(numbers)
