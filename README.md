# Cipher Text Algorithm

## 📜 Introduction

Alrighty, folks, here’s the deal: this is a super simple encryption algorithm that uses a private key to encrypt data. I made the key public here (so, no, you can't go breaking into top-secret vaults with this), but the idea is to demonstrate the basics of encryption. Not the most impossible-to-crack system, but it should keep most normal folks (and machines) scratching their heads for a while. 😎

Forget the days of high-tech quantum computing... for now, anyway. This algorithm will likely drive your average person mad (in a good way) without a key, but hey, it won’t stop the pro hackers! 🙄💻

## 🔑 How Does It Work?

The concept behind this is so simple you’ll wonder why you didn’t think of it first! But here’s how we encrypt your text:

1. **Step 1: Alphabet Assignment**
    We assign each letter of the alphabet to a corresponding serial number, like this:
    `A = 1`, `B = 2`, `C = 3`... you get the idea, right?
2. **Step 2: The Key**
    We take our private key (let’s call it "Key" for this example). The letters of the key are mapped to the alphabetic serial number, just like in Step 1.
3. **Step 3: Right Shift!**
    Now, the magic happens: we take each letter of the text you want to encrypt and right-shift it by a number corresponding to the letter in the key. For example:

    - The letter `A` might be shifted by `3` (because `C = 3` in our key).
    - The letter `B` might be shifted by `5` (because `E = 5` in our key).
    - And so on!

    The final encrypted text? A jumbled mess of letters that only someone with the correct key can decrypt. It’s like hiding a message in plain sight—well, kinda. 😉
4. **Step 4: Decryption (or not)**
    To decrypt, you would simply reverse the process: use the same key and left-shift the letters back to their original positions.

It's that simple. No high-level cryptography degree required (but you’ll still feel like a secret agent while using it). 🕵️‍♂️


## 🖥️ Example

Let’s say our private key is `"KEY"` and we’re encrypting the message `"HELLO WORLD!"`. Here’s how it works:

- **Key mapping:**
    - `K = 11`, `E = 5`, `Y = 25`
- **Text to encrypt:**
    - `"HELLO WORLD!"`
- **Shift each letter by the corresponding key values:**
    - `H` (shifted by `11`) -> `S`
    - `E` (shifted by `5`) -> `J`
    - `L` (shifted by `25`) -> `J`
    - `L` (shifted by `11`) -> `W`
    - `O` (shifted by `5`) -> `T`
    - And so on...

The result: **"SJJWZ VSCQF!"**

It looks like someone just hit the keyboard, but trust me, there's some logic behind this. 😅


## 🤔 Why Should You Care?

Great question, my friend. You don’t need to care about this (unless you want to make sure your top-secret pizza order doesn’t get leaked to your roommate... again). 🍕

However, learning basic encryption techniques like this gives you an insight into how cryptography works on a very basic level, and hey, it's a fun way to play around with numbers and letters!

Plus, it’ll impress your friends when you casually start encrypting your text messages. “Why yes, I do keep my cat memes secure with a personal encryption algorithm. Why do you ask?” 😎

## 💡 Key Features:

- **Simple to understand:** You don’t need to be a tech wizard to grasp this.

- **Customizable key:** Use any key you want (well, within reason... maybe not "password", ok?).

- **Easy encryption/decryption:** Encrypt your messages like a pro and reverse the process like a champ.

- **Fun and educational:** You get to feel like a cryptographer without the need for any hacking skills. 🖤


## 🎉 Final Thoughts

While this encryption method is definitely not "unbreakable" (I mean, come on, I’m not trying to win the Nobel Prize here), it’s a fun little tool to get into the world of cryptography. Plus, you’ll get to feel like a secret agent. 🕶

Just don’t try encrypting your entire shopping list with this for national security... or do, if you’re into that. 😆

And remember, no system is foolproof—except your secret cookie recipe. 🍪

## Usage

1. Clone the repository
```bash
git clone https://github.com/AnirbanNath-dev/Cipher-text-algorithm.git
```

2. Change the directory 
```bash
cd Cipher-text-algorithm
```
**Note: If you are in windows , simply run it by `python main.py`. If you are in linux/unix-based system, you can follow the later steps**


```bash
chmod +x exec.py
```

```bash
./exec.py -h #help 
./exec.py -e any_text #to encode
./exec.py -d encoded_text #to decode
```


