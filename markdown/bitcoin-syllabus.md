# Bitcoin Protocol Development Curriculum 
## **Chaincode Labs | [(Source)](https://github.com/chaincodelabs/bitcoin-curriculum)**
---

- ## Introduction

    - [ ] 📒 [**Bitcoin White Paper**](https://bitcoin.org/bitcoin.pdf)

    - [ ] 📝 [**If I'd Known What We Were Starting (2017)**](https://www.linkedin.com/pulse/id-known-what-we-were-starting-ray-dillinger/)

    - [ ] 📝 [**Bitcoin's Academic Pedigree (2017)**](https://queue.acm.org/detail.cfm?id=3136559)

    - [ ] 🎥 [**Intro to Blockchain**](https://www.youtube.com/watch?v=on5ySFK0aoY)

    - [ ] 📒 [**The Economic Limits of Bitcoin and the Blockchain**](https://faculty.chicagobooth.edu/eric.budish/research/Economic-Limits-Bitcoin-Blockchain.pdf)

    - [ ] 📝 [**The Anatomy of Proof-of-Work**](https://bitcointechtalk.com/the-anatomy-of-proof-of-work-98c85b6f6667)

    - [ ] 📒 [**Bitcoin Developer Reference**](https://www.lopp.net/pdf/Bitcoin_Developer_Reference.pdf)

    - [ ] 🌐 [**Difficulty adjustment**](https://bitcoin.stackexchange.com/questions/855/what-keeps-the-average-block-time-at-10-minutes/857#857)

    - [ ] 📒 [**The Byzantine Generals Problem**](http://diyhpl.us/~bryan/papers2/bitcoin/The%20Byzantine%20generals%20problem%20-%20Lamport%20-%201982.pdf)

    - [ ] 💬 [**Running a full node**](https://www.reddit.com/r/BitcoinBeginners/comments/3eq3y7/full_node_question/ctk4lnd/)

- ## History & Philosophy of Bitcoin

    - [ ] 📝 [**The Incomplete History of Bitcoin Development**](https://b10c.me/blog/004-the-incomplete-history-of-bitcoin-development/)

    - [ ] 🎥 [**What is Consensus?**](https://www.youtube.com/watch?v=fw3WkySh_Ho)

- ## Soft Forks & Protocol Overview

    - [ ] 📝 [**On Unstoppability of Softforks**](https://zmnscpxj.github.io/bitcoin/unpreventable-softforks.html)

    - [ ] **Upgrading the protocol**

        TODO 

    - [ ] 📝 [**Example soft forks**](https://en.bitcoin.it/wiki/Softfork)

    - [ ] 📝 [**Forks, Signaling, and Activation**](https://medium.com/@elombrozo/forks-signaling-and-activation-d60b6abda49a)

    - [ ] 📝 [**Better Fork Terminology**](http://www.truthcoin.info/blog/protocol-upgrade-terminology/)

    - [ ] 📝 [**Forced Soft Forks**](https://petertodd.org/2016/forced-soft-forks)

    - [ ] 📝 [**Flag day upgrades**](https://medium.com/@bergealex4/uasf-user-driven-protocol-development-da4e886832d)

    - [ ] 📑 [**IsSuperMajority signaling - BIP 65 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)

    - ### BIP 9

        - [ ] 📝 [**BIP9: versionbits In a Nutshell**](https://rusty.ozlabs.org/?p=576)

        - [ ] 📑 [**BIP9 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)

    - ### BIP148 and BIP149

        - [ ] 📑 [**BIP 148 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki)

        - [ ] 📑 [**BIP 149 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0149.mediawiki)

        - [ ] 📝 [**UASF BIP148 Scenarios and Game Theory**](https://medium.com/@jimmysong/uasf-bip148-scenarios-and-game-theory-9530336d953e)

        - [ ] 📝 [**User Activated Soft Forks: the BIP 148 alternative**](https://segwit.org/user-activated-soft-forks-the-bip-148-alternative-28e87ffdb76f)

    - [ ] 📑 [**BIP91**](https://github.com/bitcoin/bips/blob/master/bip-0091.mediawiki)

- ## Security Models

    - ### Overview

        - [ ] 📝 [**Overview of Security Concerns**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/overview-of-security-concerns/)

        - [ ] 🎥 [**Danger! Bitcoin Threat Models**](https://vimeo.com/316625785#t=750s)

        - [ ] 📝 [**Bitcoin’s Security Model: A Deep Dive**](https://www.coindesk.com/bitcoins-security-model-deep-dive)

        - [ ] 📝 [**Bitcoin Weaknesses**](https://en.bitcoin.it/wiki/Weaknesses)

        - [ ] 📒 [**Speed-Security Tradeoffs in Blockchain Protocols**](https://pdfs.semanticscholar.org/ac1a/918fc933b767d34574ec2cc6a33b4223dc1a.pdf)

    - ### Checkpoints, assumevalid, minimumchainwork

        - [ ] 📝 [**Bitcoin's Diversity of Use-Cases and Security Models**](https://bluematt.bitcoin.ninja/2017/02/28/bitcoin-trustlessness/)

        - [ ] 🐦 [**Dave Harding Tweet on assumed valid blocks and minimum chainwork**](https://twitter.com/hrdng/status/869206705548271616)

    - [ ] 📑 [**Defining SPV and lightclients**](https://gist.github.com/ariard/1034cd7624805d53334e80d4712fb8ee)

    - ### BIP 37 (bloom filters)

        - [ ] 📑 [**BIP 39 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0037.mediawiki)

        - [ ] 📒 [**On the Privacy Provisions of Bloom Filters in Lightweight Bitcoin Clients**](https://eprint.iacr.org/2014/763.pdf)

    - ### Neutrino

        - [ ] 📑 [**BIP 157 Spec**](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)

        - [ ] 📝 [**Neutrino: The Lighter Side of Lightning**](https://blog.lightning.engineering/posts/2018/10/17/neutrino.html)

        - [ ] 💬 [**Index for BIP 157 block filters**](https://github.com/bitcoin/bitcoin/pull/14121)

        - [ ] 🎥 [**Exploring Neutrino**](https://vimeo.com/316626387)

    - [ ] 📑 [**Committed bloom filters**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-May/012636.html)

    - ### Fraud proofs

        - [ ] 📝 [**Fraud Proofs - Mustafa Al-Bassam**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/tokyo-2018/fraud-proofs/)

        - [ ] 📑 [**Fraud Proofs: Improving the ability of SPV clients to detect invalid chains**](https://gist.github.com/justusranvier/451616fa4697b5f25f60)

        - [ ] 💬 [**Bitcoin Wizards Fraud Proof thread**](https://people.xiph.org/~greg/bitcoin-wizards-fraud-proof.log.txt)

        - [ ] 💬 [**Improving SPV security with PoW fraud proofs**](https://www.mail-archive.com/bitcoin-dev@lists.linuxfoundation.org/msg07913.html)

    - [ ] 💬 [**Committed UTXO hashes**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-October/011638.html)

    - [ ] 📑 [**Assume UTXO FAQ**](https://github.com/jamesob/assumeutxo-docs/tree/2019-04-proposal/proposal)

- ## Mining

    - [ ] 📝 [**Poisson distribution/Progress-free-ness**](https://towardsdatascience.com/the-poisson-distribution-and-poisson-process-explained-4e2cb17d459)

    - [ ] 📒 [**Block arrivals in the Bitcoin blockchain**](https://arxiv.org/pdf/1801.07447.pdf)

    - [ ] 💬 [**Fee Sniping**](https://www.reddit.com/r/Bitcoin/comments/47upgx/nsequence_and_optin_replacebyfee_difference/d0g612x/?context=5)

    - ### Selfish Mining

        - [ ] 📒 [**On the Instability of Bitcoin Without the Block Reward**](https://www.cs.princeton.edu/~smattw/CKWN-CCS16.pdf)

        - [ ] 📒 [**Majority is not Enough: Bitcoin Mining is Vulnerable**](https://www.cs.cornell.edu/~ie53/publications/btcProcFC.pdf)

        - [ ] 📝 [**How to mine bitcoin profitably (2015)**](https://scalingbitcoin.org/transcript/montreal2015/how-to-mine-bitcoin-profitably)

        - [ ] 📝 [**Why Bitcoin Mining Pools Aren’t Incentivized To Broadcast Blocks Quickly**](https://bitcoinmagazine.com/articles/why-bitcoin-mining-pools-aren-t-incentivized-to-broadcast-blocks-quickly-1475249510)

        - [ ] 📒 [**Optimal Selfish Mining Strategies in Bitcoin**](http://diyhpl.us/~bryan/papers2/bitcoin/Optimal%20selfish%20mining%20strategies%20in%20bitcoin.pdf)

        - [ ] 📝 [**If There Is An Answer To Selfish Mining, Braiding Could Be It**](https://bitcoinmagazine.com/articles/if-there-is-an-answer-to-selfish-mining-braiding-could-be-it-1482876153)

    - [ ] 📝 [**51% attacks**](https://medium.com/chainrift-research/bitcoins-attack-vectors-51-attacks-a96deac43774)

    - [ ] 📝 [**BetterHash**](https://github.com/TheBlueMatt/bips/blob/betterhash/bip-XXXX.mediawiki)

    - [ ] 📒 [**No Reward Mining Overview**](https://www.cs.princeton.edu/~smattw/CKWN-CCS16.pdf)

    - [ ] 📒 [**Pool Overview**](http://diyhpl.us/~bryan/papers2/bitcoin/Analysis%20of%20Bitcoin%20pooled%20mining%20reward%20systems%20-%20Rosenfeld%20-%202011.pdf)

    - [ ] 💬 [**Pool Hopping**](https://bitcointalk.org/index.php?topic=39832)

    - [ ] 🌐 [**PPS As a Real-World Business Solution**](https://en.bitcoin.it/wiki/Pooled_mining#The_Pay-per-Share_approach)

        Specifically the section on the Pay per Share Share_approach

    - [ ] 📝 [**Trustless Pools**](https://en.bitcoin.it/wiki/P2Pool)

    - [ ] 💬 [**Payment Channel Payouts**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-August/014893.html)

    - ### ASICBoost

        - [ ] 📒 [**AsicBoost: A Speedup for Bitcoin Mining**](https://arxiv.org/pdf/1604.00575.pdf)

        - [ ] 📒 [**The Problem with ASICBOOST**](http://www.mit.edu/~jlrubin//public/pdfs/Asicboost.pdf)

        - [ ] 💬 [**Inhibiting a covert attack on the Bitcoin POW function**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-April/013996.html)

    - ### BCH Mining/Difficulty Adjustment

        - [ ] 📝 [**Bringing Stability to Bitcoin Cash Difficulty Adjustments**](https://medium.com/@Mengerian/bringing-stability-to-bitcoin-cash-difficulty-adjustments-eae8def0efa4)

        - [ ] 📝 [**Bitcoin Cash Difficulty Adjustments**](https://medium.com/@jimmysong/bitcoin-cash-difficulty-adjustments-2ec589099a8e)

        - [ ] 📝 [**Difficulty Adjustment Algorithm Update**](https://www.bitcoinabc.org/2017-11-01-DAA/)

    - [ ] 📒 [**TumbleBit**](https://open.bu.edu/bitstream/handle/2144/29224/575.pdf?sequence=2&isAllowed=y)

- ## Attacks

    - [ ] 📝 [**Dust Attacks**](https://medium.com/chainrift-research/bitcoins-attack-vectors-dust-attacks-9040edee2986)

- ## Consensus approaches

    - [ ] 📝 [**Overview**](https://medium.com/scalar-capital/on-consensus-e47920cd8914)

    - ### GHOST

        - [ ] 📝 [**The GHOSTDAG protocol**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/tokyo-2018/ghostdag/)

        - [ ] 📒 [**Secure High-Rate Transaction Processing in Bitcoin**](https://eprint.iacr.org/2013/881.pdf)

        - [ ] 📑 [**Modified GHOST Implementation in Ethereum**](https://github.com/ethereum/wiki/wiki/White-Paper#modified-ghost-implementation)

    - [ ] 📝 [**Braiding**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/hong-kong/braiding-the-blockchain/)

    - [ ] 📝 [**Byzantine Fault Tolerance**](https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419)

    - [ ] 📝 [**Bitcoin-NG**](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf)

    - ### Proof of Stake

        - [ ] 📝 [**Proof of Work & Proof of Stake**](https://medium.com/loom-network/understanding-blockchain-fundamentals-part-2-proof-of-work-proof-of-stake-b6ae907c7edb)

        - [ ] 📝 [**Proof-of-Stake & the Wrong Engineering Mindset**](https://medium.com/@hugonguyen/proof-of-stake-the-wrong-engineering-mindset-15e641ab65a2)

    - ### Sidechains

        - [ ] 📒 [**Enabling Blockchain Innovations with Pegged Sidechains**](https://blockstream.com/sidechains.pdf)

        - [ ] 📝 [**Paul Storzc on Sidechains**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/milan/sidechains/)

        - [ ] 📒 [**Proof-of-Work Sidechains**](http://diyhpl.us/~bryan/papers2/bitcoin/Proof-of-Work%20sidechains%20-%202018.pdf)

- ## Consensus Changes & Hard Forks

    - [ ] 📝 [**A complete history of Bitcoin’s consensus forks**](https://blog.bitmex.com/bitcoins-consensus-forks/)

    - ### Extension blocks

        - [ ] 💬 [**Auxiliary block: Increasing max block size with softfork**](https://bitcointalk.org/index.php?topic=283746.0)

        - [ ] 📝 [**How Bitcoin Extension Blocks Are Backward Compatible — and How They’re Not**](https://bitcoinmagazine.com/articles/how-extension-blocks-are-backward-compatible-and-how-theyre-not)

    - [ ] 📝 [**Hard forks: Potential dangers**](https://medium.com/@jimmysong/network-partitioning-321b7f159868)

    - ### Replay Protection

        - [ ] 📝 [**Replay Attacks Explained**](https://bitcointechtalk.com/replay-attacks-explained-e3d6d2ea0ab2)

        - [ ] 📝 [**How to Protect Against Replay Attacks**](https://bitcointechtalk.com/how-to-protect-against-replay-attacks-7a00bd2fe52f)

        - [ ] 💻 [**2017_optin_replay code on btc1**](https://github.com/btc1/bitcoin/commit/a3c41256984bf11d95a560ae89c0fcbadfbe73dc)

    - [ ] **Wipeout Protection**

        TODO 

    - [ ] 🌐 [**Light Nodes**](https://en.bitcoin.it/wiki/Lightweight_node)

    - [ ] 📑 [**Spoonnet: another experimental hardfork**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-February/013542.html)

- ## Cryptography

    - [ ] 📝 [**The 3 Seminal Events In Cryptography**](http://doctrina.org/The-3-Seminal-Events-In-Cryptography.html)

    - [ ] 📒 [**An Overview of Public Key Cryptography**](https://ee.stanford.edu/~hellman/publications/31.pdf)

    - ### Finite fields, Elliptic Curves, ECDSA, Schnorr

        - [ ] 🎥 [**Dev++ 02-01-EN | Finite fields, Elliptic Curves, ECDSA, Schnorr - John Newbery | Cryptography**](https://www.youtube.com/watch?v=DcGm_4-ig1o)

        - [ ] 📝 [**Elliptic Curve Cryptography Explained**](https://fangpenlin.com/posts/2019/10/07/elliptic-curve-cryptography-explained/)

    - [ ] 📝 [**Bitcoin, Chance and Randomness**](https://medium.com/@hugonguyen/bitcoin-chance-and-randomness-ba49a6edf933)

    - [ ] 📝 [**libsecp**](https://scalingbitcoin.org/transcript/stanford2017/state-of-cryptography)

    - [ ] 📝 [**State of cryptography for blockchains beyond ECDSA and sha256**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/stanford-2017/state-of-cryptography/)

    - [ ] 📒 [**On Bitcoin Security in the Presence of Broken Crypto Primitives**](http://diyhpl.us/~bryan/papers2/bitcoin/On%20Bitcoin%20security%20in%20the%20presence%20of%20broken%20crypto%20primitives%20-%202016.pdf)

    - ### Zero Knowledge proofs

        TODO add more

        - [ ] 🎥 [**Introduction to Snarks**](https://www.youtube.com/watch?v=jr95o_k_SwI&feature=youtu.be)

    - ### Bulletproofs

        - [ ] 📝 [**How Bulletproofs Could Make Bitcoin Privacy Less Costly**](https://bitcoinmagazine.com/articles/how-bulletproofs-could-make-bitcoin-privacy-less-costly)

        - [ ] 📝 [**Bulletproofs: Faster Rangeproofs and Much More**](https://bitcoinmagazine.com/articles/how-bulletproofs-could-make-bitcoin-privacy-less-costly)

        - [ ] 📝 [**Bulletpoints on bulletproofs**](https://joinmarket.me/blog/blog/bulletpoints-on-bulletproofs/)

        - [ ] 📒 [**From Zero Knowledge Proofs to Bulletproofs Paper**](https://joinmarket.me/blog/blog/from-zero-knowledge-proofs-to-bulletproofs-paper/)

        - [ ] 📝 [**Building on Bulletproofs**](https://medium.com/@cathieyun/building-on-bulletproofs-2faa58af0ba8)

    - ### Commitment schemes; pedersen commitments

        - [ ] 📝 [**Commitment schemes**](https://storage.googleapis.com/dev.adjoint.io/crypto.html#commitment-schemes)

        - [ ] 📒 [**Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing**](https://www.cs.cornell.edu/courses/cs754/2001fa/129.PDF)

    - ### Schnorr

        - [ ] 🎥 [**Introduction to Schnorr Signatures with Elichai Turkel**](https://www.youtube.com/watch?v=XKatSGCZ-gE&feature=youtu.be)

        - [ ] 📒 [**Simple Schnorr Multi-Signatures with Applications to Bitcoin**](https://eprint.iacr.org/2018/068.pdf)

        - [ ] 📝 [**Liars, cheats, scammers and the Schnorr signature**](https://joinmarket.me/blog/blog/liars-cheats-scammers-and-the-schnorr-signature/)

    - [ ] 📝 [**Diffie-Hellman Key Exchange: A Non-mathematician’s explanation**](https://community.cisco.com/legacyfs/online/legacy/3/5/6/26653-dh.PDF)

    - [ ] 📝 [**Ring Signatures**](https://joinmarket.me/blog/blog/ring-signatures/)

    - [ ] 📝 [**How RSA Works With Examples**](http://doctrina.org/How-RSA-Works-With-Examples.html)

- ## Transactions

    - [ ] 📝 [**Understanding a Raw Bitcoin Transaction**](https://medium.com/@marchtodeath/understanding-a-raw-bitcoin-transaction-531193b7e147)

    - [ ] 📋 [**Bitcoins the hard way: Using the raw Bitcoin protocol**](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)

    - [ ] 📝 [**Working with transactions**](https://bitcoinj.github.io/working-with-transactions)

    - [ ] 💻 [**Transaction format – IsMine function in Bitcoin Core**](https://github.com/bitcoin/bitcoin/blob/624bee96597c1d59018e58131b8285c0b332700d/src/script/ismine.cpp#L43)

    - ### Script

        - [ ] 📖 [**Bitcoin Developer Reference**](https://www.lopp.net/pdf/Bitcoin_Developer_Reference.pdf#page=19)

            Section 4.2

        - [ ] 🎥 [**Advanced Bitcoin Scripting: Transactions & Multisig**](https://www.youtube.com/watch?v=8FeAXjkmDcQ)

    - ### Signing transactions

        - [ ] 💬 [**Why the signature is always 65 (1+32+32) bytes long?**](https://bitcoin.stackexchange.com/questions/12554/why-the-signature-is-always-65-13232-bytes-long/12556#12556)

    - ### Standardness

        - [ ] 📖 [**Bitcoin Developer Reference**](https://www.lopp.net/pdf/Bitcoin_Developer_Reference.pdf#page=16)

            Section 3.3

        - [ ] 📝 [**The Bitcoin Non-standard**](https://medium.com/summa-technology/the-bitcoin-non-standard-6103330af98c)

        - [ ] 💻 [**Definition of Standardness**](https://github.com/libbitcoin/libbitcoin-server/wiki/Standardness)

    - ### 0-conf transactions

        - [ ] 📝 [**Support for zero-confirmation transactions at Bitcoin ATM**](https://coinatmradar.com/blog/support-zero-confirmation-transactions-at-bitcoin-atm/)

        - [ ] 📑 [**Solving the 0-conf problem using forfeits**](https://gist.github.com/awemany/619a5722d129dec25abf5de211d971bd)

    - ### Partially Signed Bitcoin Transactions

        - [ ] 🎥 [**Andrew Chow: Partially Signed Bitcoin Transactions**](https://www.youtube.com/watch?v=H6xZSRDXUiU)

        - [ ] 📑 [**BIP 174**](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

        - [ ] 📝 [**PSBT (BIP 174) - Partially Signed Bitcoin Transactions**](https://bitcointechweekly.com/front/bip-174-psbt-partially-signed-bitcoin-transactions/)

        - [ ] 📋 [**PSBT Howto for Bitcoin Core**](https://github.com/bitcoin/bitcoin/blob/master/doc/psbt.md)

        - [ ] 💬 [**Partially Signed Bitcoin Transaction (PSBT) format**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-August/014843.html)

    - [ ] 💬 [**SIGHASH_NOINPUT**](https://bitcoin-development.narkive.com/PhL7HxZZ/bip-sighash-noinput)

    - [ ] 📑 [**Compacted Transactions**](https://people.xiph.org/~greg/compacted_txn.txt)

    - ### Mempool

        - [ ] 📝 [**How the Mempool Works**](https://blog.kaiko.com/an-in-depth-guide-into-how-the-mempool-works-c758b781c608)

        - [ ] 📝 [**Transaction Pools**](https://github.com/bitcoinbook/bitcoinbook/blob/f8b883dcd4e3d1b9adf40fed59b7e898fbd9241f/ch08.asciidoc#transaction-pools)

            This is a snippet from the `bitcoinbook` project

        - [ ] 🎥 [**Bitcoin p2p network**](https://www.youtube.com/watch?v=eVerdR2hOMw&feature=youtu.be&t=1918)

            Starts at 31:58

- ## Blocks

    - ### Merkle Trees

        - [ ] 📖 [**Bitcoin Developer Reference**](https://www.lopp.net/pdf/Bitcoin_Developer_Reference.pdf#page=5)

            Section 2.2

        - [ ] 📒 [**Weaknesses in Bitcoin’s Merkle Root Construction**](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/attachments/20190225/a27d8837/attachment-0001.pdf)

    - [ ] 📝 [**Data structures in validation**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/validation-costs/)

    - [ ] 🎥 [**Handling Re-orgs & Forks**](https://www.youtube.com/watch?time_continue=839&v=wtTQ_1WyUoY)

        Starts at 13:59

    - ### Pruning

        - [ ] 📑 [**Block file pruning**](https://bitcoin.org/en/release/v0.11.0#block-file-pruning)

        - [ ] 💻 [**Add autoprune functionality PR #5863**](https://github.com/bitcoin/bitcoin/pull/5863)

- ## SegWit

    - ### Introduction

        - [ ] 📝 [**Understanding Segregated Witness**](https://segwit.org/understanding-segregated-witness-905cc712c692)

        - [ ] 📝 [**Segregated Witness**](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch07.asciidoc#segregated-witness)

        - [ ] 🎥 [**Bitcoin Protocol Design: Segregated Witness Revisited**](https://www.youtube.com/watch?v=AjBpIkfB-ac)

        - [ ] 🎥 [**SegWit**](https://www.youtube.com/watch?v=Txfy2mFe16A)

        - [ ] 📝 [**Segregated Witness Benefits**](https://bitcoincore.org/en/2016/01/26/segwit-benefits/)

        - [ ] 📝 [**Segregated Witness Costs and Risks**](https://bitcoincore.org/en/2016/10/28/segwit-costs/)

        - [ ] 📝 [**The Long Road To SegWit: How Bitcoin’s Biggest Protocol Upgrade Became Reality**](https://bitcoinmagazine.com/articles/long-road-segwit-how-bitcoins-biggest-protocol-upgrade-became-reality)

    - [ ] 📝 [**SegWit and scalabilty**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/hong-kong/segregated-witness-and-its-impact-on-scalability/)

    - ### Tx malleability

        - [ ] 📝 [**Transaction Malleability Explained**](https://bitcointechtalk.com/transaction-malleability-explained-b7e240236fc7)

        - [ ] 🎥 [**SF Bitcoin Devs Seminar: Transaction Malleability: Threats and Solutions**](https://www.youtube.com/watch?v=jyDE-aFqJTs)

        - [ ] 📝 [**The Who, What, Why And How Of The Ongoing Transaction Malleability Attack**](https://bitcoinmagazine.com/articles/the-who-what-why-and-how-of-the-ongoing-transaction-malleability-attack-1444253640)

        - [ ] 📑 [**Dealing with Malleability**](https://github.com/bitcoin/bips/blob/master/bip-0062.mediawiki)

        - [ ] 📒 [**Bitcoin Transaction Malleability and MtGox**](https://arxiv.org/pdf/1403.6676.pdf)

    - [ ] 📝 [**Understanding Segwit Block Size**](https://medium.com/@jimmysong/understanding-segwit-block-size-fd901b87c9d4)

    - [ ] 📝 [**New address type for segwit addresses**](https://diyhpl.us/wiki/transcripts/sf-bitcoin-meetup/2017-03-29-new-address-type-for-segwit-addresses/)

    - [ ] 📝 [**Segregated Witness Wallet Development Guide**](https://bitcoincore.org/en/segwit_wallet_dev/)

- ## Wallets

    - ### HD Wallet

        - [ ] 📑 [**BIP 32 - Hierarchical Deterministic Wallet**](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)

        - [ ] 📑 [**BIP 44 - Multi-Account Hierarchy for Deterministic Wallets**](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)

        - [ ] 📑 [**HD Wallets Explained: From High Level to Nuts and Bolts**](https://medium.com/bitcraft/hd-wallets-explained-from-high-level-to-nuts-and-bolts-9a41545f5b0)

    - [ ] 💬 [**Wallet BerkeleyDB key value store, data file, environment, logs, flushing**](https://bitcoin.stackexchange.com/questions/51435/migration-from-berkeley-db-to-leveldb)

    - [ ] 📝 [**Wallets and Accounts and Keys, Oh My!**](https://bcoin.io/guides/wallets.html)

    - ### Wallet key management

        TODO add more on key and address metadata

        - [ ] 💬 [**Understanding keypool in Bitcoin Core**](https://bitcointalk.org/index.php?topic=2940114.msg30228579#msg30228579)

        - [ ] 📝 [**Understanding the Gap Limit**](https://blog.blockonomics.co/bitcoin-what-is-this-gap-limit-4f098e52d7e1)

    - [ ] 📝 [**How to rescan / reindex wallet?**](https://coinguides.org/rescan-reindex-wallet/)

    - [ ] 📝 [**Segregated Witness Wallet Development Guide**](https://bitcoincore.org/en/segwit_wallet_dev/)

    - ### Fees

        - [ ] 📝 [**The Fee Market Explained**](https://medium.com/@jimmysong/the-fee-market-explained-76b294947b42)

        - [ ] 📝 [**How wallets can handle transaction fees**](https://medium.com/@bramcohen/how-wallets-can-handle-transaction-fees-ff5d020d14fb)

    - ### Replace by Fee

        - [ ] 📝 [**BIP 125 - Opt-in Full Replace-by-Fee Signaling**](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)

        - [ ] 📝 [**Support for zero-confirmation transactions at Bitcoin ATM**](https://coinatmradar.com/blog/support-zero-confirmation-transactions-at-bitcoin-atm/)

    - ### Coin selection

        - [ ] 🎥 [**Unspent Management and Coin Selection**](https://www.youtube.com/watch?v=hrlNN3BSB6w)

        - [ ] 🎥 [**Coin Selection - Karl Johan Alm**](https://www.youtube.com/watch?v=MT0gpRG2elY)

        - [ ] 📝 [**Coin Selection (Scaling 2016)**](https://scalingbitcoin.org/transcript/milan2016/coin-selection)

        - [ ] 📒 [**An Evaluation of Coin Selection Strategies**](http://murch.one/wp-content/uploads/2016/11/erhardt2016coinselection.pdf)

    - [ ] 🎥 [**Using your hardware wallet with Bitcoin Core**](https://vimeo.com/316634495)

- ## Scripts and Contracts

    - [ ] 🎥 [**Scripts - general & simple**](https://www.youtube.com/watch?v=np-SCwkqVy4)

    - [ ] 🎥 [**P2PKH, P2WPKH, P2SH, P2WSH**](https://www.youtube.com/watch?time_continue=8&v=nrYOMjVmqi8)

    - [ ] 🎥 [**Bitcoin Multisig and P2SH Transactions with Andreas Antonopoulos**](https://www.youtube.com/watch?v=K-ccC9YZ8UI)

    - ### Script Descriptors

        - [ ] 📝 [**Script descriptors**](http://diyhpl.us/wiki/transcripts/bitcoin-core-dev-tech/2018-10-08-script-descriptors/)

        - [ ] 📑 [**Support for Output Descriptors in Bitcoin Core**](https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md)

    - [ ] 📝 [**Improving Privacy Using Pay-to-EndPoint (P2EP)**](https://blockstream.com/2018/08/08/en-improving-privacy-using-pay-to-endpoint/)

    - ### Smart Contracts on a Dumb Chain

        - [ ] 📝 [**MimbleWimble**](https://medium.com/scalar-capital/behind-mimblewimble-cd9da78a00e9)

        - #### Scriptless Scripts

            - [ ] 💻 [**ElementsProject/scriptless-Scripts**](https://github.com/ElementsProject/scriptless-scripts/tree/master/md)

            - [ ] 📝 [**Scriptless Scripts - A different kind of smart contract**](https://medium.com/scalar-capital/scriptless-scripts-25e18fd52ede)

            - [ ] 🎥 [**Scriptless scripts, adaptor signatures and their applications**](https://www.youtube.com/watch?time_continue=2&v=PDzGP621pEs)

    - ### Payment Channels

        - [ ] 📝 [**Understanding Payment Channels**](https://blog.chainside.net/understanding-payment-channels-4ab018be79d4)

        - [ ] 🎥 [**Bitcoin Protocol Design: Payment Channels Revisited**](https://www.youtube.com/watch?v=4SdBa8ZOfqg)

        - [ ] 📝 [**Bitcoin script v2.0**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/stanford-2017/bitcoin-script-v2.0-and-strengthened-payment-channels/)

    - ### MAST

        - [ ] 📝 [**What is a Bitcoin Merklized Abstract Syntax Tree (MAST)?**](https://bitcointechtalk.com/what-is-a-bitcoin-merklized-abstract-syntax-tree-mast-33fdf2da5e2f)

        - [ ] 📝 [**Merkleized abstract syntax trees (MAST)**](http://diyhpl.us/wiki/transcripts/bitcoin-core-dev-tech/2017-09-07-merkleized-abstract-syntax-trees/)

        - [ ] 📝 [**MAST Discussion**](https://diyhpl.us/wiki/transcripts/bitcoin-core-dev-tech/2018-03-06-merkleized-abstract-syntax-trees-mast/)

    - ### ZK SNARKS

        - [ ] 📝 [**Scaling Bitcoin – Snarks Panel**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/snarks/)

        - [ ] 📝 [**Introduction to SNARKs**](https://www.youtube.com/watch?v=jr95o_k_SwIs)

        - [ ] 📝 [**STARKs, Part I: Proofs with Polynomials**](https://vitalik.ca/general/2017/11/09/starks_part_1.html)

    - ### ZK STARKs

        - [ ] 📒 [**Scalable, transparent, and post-quantum secure computational integrity**](https://eprint.iacr.org/2018/046.pdf)

        - [ ] 📝 [**STARKs, Part II: Thank Goodness It's FRI-day**](https://vitalik.ca/general/2017/11/22/starks_part_2.html)

        - [ ] 📝 [**STARKs, Part 3: Into the Weeds**](https://vitalik.ca/general/2018/07/21/starks_part_3.html)

        - [ ] 📝 [**ZK-STARKs — Create Verifiable Trust, even against Quantum Computers**](https://medium.com/coinmonks/zk-starks-create-verifiable-trust-even-against-quantum-computers-dd9c6a2bb13d)

    - ### ZK STARKs

        - [ ] 🎥 [**Tadge Dryja: Discreet Log Contracts**](https://www.youtube.com/watch?v=FU-rA5dkTHI&feature=emb_logo)

        - [ ] 📝 [**Discreet Log Contracts: invisible smart contracts on the Bitcoin blockchain**](https://medium.com/@gertjaap/discreet-log-contracts-invisible-smart-contracts-on-the-bitcoin-blockchain-cc8afbdbf0db)

        - [ ] 📝 [**STARKs, Part 3: Into the Weeds**](https://vitalik.ca/general/2018/07/21/starks_part_3.html)

        - [ ] 📝 [**ZK-STARKs — Create Verifiable Trust, even against Quantum Computers**](https://medium.com/coinmonks/zk-starks-create-verifiable-trust-even-against-quantum-computers-dd9c6a2bb13d)

    - ### Miniscript

        - [ ] 📝 [**Stanford Blockchain Conference 2019 - Miniscript**](http://diyhpl.us/wiki/transcripts/stanford-blockchain-conference/2019/miniscript/)

        - [ ] 📑 [**Policy to Miniscript compiler**](http://bitcoin.sipa.be/miniscript/)

    - [ ] 📑 [**The State of Script**](https://diyhpl.us/wiki/transcripts/scalingbitcoin/tokyo-2018/bitcoin-script/)

- ## Fungibility & Scalability

    - [ ] 🎥 [**The current state of Bitcoin fungibility (2019)**](https://vimeo.com/316635787)

    - ### On Scaling Decentralized Blockchains

        - [ ] 🌐 [**The Fundamental Tradeoff**](https://gist.github.com/chris-belcher/a8155df5051bb3e3aa96)

        - [ ] 📒 [**On Scaling Decentralized Blockchains (A Position Paper)**](http://diyhpl.us/~bryan/papers2/bitcoin/On%20scaling%20decentralized%20blockchains%20-%20A%20position%20paper.pdf)

