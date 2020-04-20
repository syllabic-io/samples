# Byzantine Fault Tolerance from the Fundamentals 
## **Zarko Milosevic**
---

- [ ] 📒 [**Consensus in the Presence of Partial Synchrony**](https://groups.csail.mit.edu/tds/papers/Lynch/jacm88.pdf)

    For me the most interesting part is model definition and the implementation of rounds. These ideas are used in all algorithms to create some sort of round structure, and is essential for termination. Consensus algorithms are not considered as most advanced but there are some nice ideas, like locking and unlocking concepts.

- [ ] 📒 [**Practical byzantine fault tolerance and proactive recovery**](http://www.pmg.csail.mit.edu/papers/bft-tocs.pdf)

- [ ] 📒 [**Fast Byzantine Consensus**](http://www.cs.cornell.edu/lorenzo/papers/Martin06Fast.pdf)

    Regarding these two papers, although they are definitely seminal, they are not necessarily easy read, and they don't in a clear way express core mechanisms. Regarding PBFT, the most important idea (in my view) is implementing Byzantine-tolerant consensus without signatures. But this mechanism is hidden in the SMR algorithm. This might be useful to know in the context of quantum-resistant algorithms as only assumes secure point-to-point computation. Proactive recovery part has some cool ideas in the context of snapshotting and catch-up of algorithms. The other paper is simpler read, but I am not sure it also explains the idea as simple as possible, as for example it relies on the signatures which is not needed in case of 5f+1. Signature vs signature-free was big deal in the past as algorithms were mostly designed for LAN, and there the cost of signatures matters a lot."

    

- [ ] 📒 [**Unifying Byzantine Consensus Algorithms with Weak Interactive Consistency**](https://infoscience.epfl.ch/record/140295)

    This is a paper I was involved that extract core consensus mechanism of both of these algorithms and present it in a simpler way using DLS round based model.

- ## Atomic broadcast reduction to consensus

    - [ ] 📒 [**From Byzantine Consensus to BFT State Machine Replication: A Latency-Optimal Transformation**](https://www.semanticscholar.org/paper/From-Byzantine-Consensus-to-BFT-State-Machine-A-Sousa-Bessani/fa27f4e4b2d8e62a70a1cebf3b352057c1b6527b)

        This is at the base of BFT-smart library.

        - [ ] 📒 [**State Machine Replication for the Masses with BFT-SMART**](http://www.di.fc.ul.pt/~bessani/publications/dsn14-bftsmart.pdf)

            This is the BFT Smart paper itself.

    - [ ] 📒 [**On the Reduction of Atomic Broadcast to Consensus with Byzantine Faults**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.363.5421&rep=rep1&type=pdf)

        In this paper we look at different consensus validity and find the optimal one for reduction to consensus.

- [ ] 📒 [**Automatic Reconfiguration for Large-Scale Reliable Storage Systems**](http://www.pmg.csail.mit.edu/papers/tdsc12.pdf)

    In the context of automatic reconfiguration in case of BFT protocols, this is nice paper.

- ## Performance attacks on leader-based protocols

    This was a hot topic a few few years ago in academia, and there are several ideas.  These papers provide a good view.

    - [ ] 📒 [**Prime: Byzantine Replication Under Attack**](http://www.cnds.jhu.edu/pub/papers/Prime_tdsc_accepted.pdf)

        This one explains the problem, although solution is not very elegant.

    - [ ] 📒 [**Bounded Delay in Byzantine-Tolerant State Machine Replication**](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.363.4986&rep=rep1&type=pdf)

        In this paper, we introduce algorithm called BFT-Mencius that is BFT variant of Mencius algorithm.  BFT-Mencius is designed to be modular, fully decentralised and to tolerate performance attacks.

        - [ ] 📒 [**Mencius: Building Efficient Replicated State Machines for WANs**](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/mao/mao_html/index.html)

            Background on the Mencius algorithm itself.

- ## Randomised Protocols

    Regarding randomised protocols, they are normally considered too slow, at least for LAN setting, but this might change. I might suggest these three

    - [ ] 📒 [**Ben-Or Algorithm**](https://allquantor.at/blockchainbib/pdf/ben1983another.pdf)

    - [ ] 📒 [**Random Oracles in Constantinople: Practical Asynchronous Byzantine Agreement using Cryptography**](https://allquantor.at/blockchainbib/pdf/cachin2000random.pdf)

    - [ ] 📒 [**The Honey Badger of BFT Protocols**](https://eprint.iacr.org/2016/199.pdf)

