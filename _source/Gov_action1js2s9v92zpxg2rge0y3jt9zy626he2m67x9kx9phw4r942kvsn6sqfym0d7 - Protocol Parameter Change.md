# Gov\_action1js2s9v92zpxg2rge0y3jt9zy626he2m67x9kx9phw4r942kvsn6sqfym0d7 \- Protocol Parameter Change

| Governance Voting Rationale |  |
| ----- | :---- |
| ![No type][image1] Type | ![No type][image1] Description |
| GAID | gov\_action1js2s9v92zpxg2rge0y3jt9zy626he2m67x9kx9phw4r942kvsn6sqfym0d7 |
| Title |  Decrease Treasury Tax from 20% to 10% |
| Type of GA |  |
| Date submitted |  13th Feb 2025 (Epoch 539\) |
| Expiration Date | 15th Mar 2025 (Epoch 546\) |

# Contents

- [1.0 Introduction](#1.0-introduction)  
  - [1.1 Summary](#1.1-summary)  
  - [1.2 Description of Governance Action](#1.2-description-of-governance-action)  
- [2.0 Discussion](#2.0-discussion)  
  - [2.1 Method](#2.1-method)  
  - [2.2 History of *tau* (*τ)*](#2.2-history-of-tau-\(τ\))  
  - [2.3 Understanding *tau* (*τ)*](#2.3-understanding-tau-\(τ\)-and-other-parameters)  
    - [2.3.1 Basic Evaluation Framework for Parameter Models](#2.3.1-basic-evaluation-framework-for-modeling-parameters)  
  - [2.4 Proposal Evaluation](#2.4-proposal-evaluation)  
- [3.0 Conclusion](#3.0-conclusion)  
- [References/Sources](#4.0-references/sources)

	

# 1.0 Introduction {#1.0-introduction}

## 1.1 Summary {#1.1-summary}

We are voting **NO** on this governance action to reduce the “treasury cut” (*tau or*   
*τ)* from 20% to 10%.

* History of the  *tau* (*τ)* parameter has not been fully represented here  
* Claims of benefit have not been treated with sufficient evidence or full examinations of context  
* The “Economic analysis” of this proposal falls short of our expectations for modeling of parameters  
* The change suggested does not align with our principles regarding navigating complexity, where change should be continuous and iterative, rather than single large movements  
* We include here recommendations for improvement, as well as a basic framework for evaluating the models we develop and use to understand things like protocol parameters

## 1.2 Description of Governance Action {#1.2-description-of-governance-action}

Protocol Parameter Changes are governance actions that implement any change to one or more updatable protocol parameters, excluding changes to major protocol versions ('hard forks').  They are divided up into four categories, however they are not exclusive of each other and a governance action may contain more than one protocol parameter update, as they often are required to be synchronized when changed.

The parameter under consideration (*tau or τ)* belongs to the **economic** category and is ratified by the **Constitutional Committee** (passed) and the **Dreps** (67% threshold).  **SPOs** do not vote on this governance action.  This parameter is referred to in several ways, including as *tau* (*τ)* in the Shelley specification and Genesis file, as “treasury expansion” in govtool documentation, as \`treasuryCut\` in CLI documentation, and as \`treasury\_growth\_rate\` in DBsync documentation.  We will be referring to it as either \`treasuryCut\` or *tau* (*τ)* depending on context.

# 2.0 Discussion {#2.0-discussion}

## 2.1 Method {#2.1-method}

We will first seek to understand the context of this governance action by investigating two elements:

* The history of the *tau* (*τ)* parameter, how it was initially set, and any changes or attempted changes that have been made to it  
* The wider understanding that is available regarding the real world performance of *tau* (*τ)*, as well as its interaction with other economic parameters

Based on the context we establish, we will then proceed to evaluate the governance action for several formal qualities and in line with several fundamental principles, including:

* Does the proposal accurately describe known facts about the parameter?  
* Does the proposal provide robust evidence for any claims it makes?  
* Is the approach to evaluating the potential of the claim rigorous?  
* StakePool rewards, an area directly affected by changes to *tau* (*τ)*, are a critical decentralization/security mechanism for Cardano, and we are biased towards the operational sustainability of those rewards when possible.  
* Promoting change in complex environments should be done in an iterative fashion with adequate resources committed to monitoring and evaluation, and clear protocols for when to rollback changes that may be causing unexpected or deleterious behavior.

## 2.2 History of *tau* (*τ)* {#2.2-history-of-tau-(τ)}

*Tau* (*τ)*  was introduced in design specifications of the Shelley era, where it was described as a necessary preset parameter to begin development of the Cardano Treasury as described in the Cardano Roadmap.  Despite not having a full treasury *(T)* system at the time, and still needing more research in order to implement one, funds would still be collected into a “*T* pot”, according to the setting of the *tau* (*τ)* parameter.

In June of 2020, [in a blog post](#iterating-for-growth-with-iohk-research), Lars Brunjes described the initial setting of the *tau* (*τ)* parameter.  Understanding that the relationships of unclaimed rewards, pledge and the monetary expansion parameters were deeply interconnected, along with assumptions about ADA adoption and target “half-life” parameters for the reserve, a steady rate of 5% was suggested for *tau* (*τ)* with unclaimed rewards going to the treasury.  Importantly, this forecast estimated that in 5 years, the treasury could be expected to harbor 2,900,000,000 ADA, and this was considered a strong case for both the incentivization of early node operators and attractive resources for future stakeholders, the key balance always being struck in the incentives mechanism.

The Shelley design specifications [(SL-D1 v.1.21, 2020/07/23)](#4.0-references/sources) include Section 5, where the modeling and design of rewards/incentives parameters is described in detail.  Here we see the complex interactions across many protocol parameters and other assumptions (including *k, F(avg tx fees), e(exchange rate), c(exp operational costs),* etc.)  *Tau* (*τ)*  itself is described in Section 5.10 as a “policy decision” with strong influence from assumptions in the *rho (ρ),* or monetary expansion, parameter.  The description of *tau* (*τ)* there is that it would be set to 20% rather than 5%, with unclaimed rewards returning to the reserve.  
In October of 2020, [in a Cardano Forum post](#double-treasury-taxation-of-40%-and-possible-workarounds), we find some insight into why the rate was changed.  Discovery of a “real tax rate” higher even than the 20% *tau* (*τ)* due to a form of “double taxation” led to a discussion around whether this “real tax rate” phenomenon was known or even intended (this “real tax rate” is describe in the forum post as 40%, however we now know it to be far more variable, especially under specific circumstances).  In comments from Lars Brunjes and Cardano Foundation representatives, several points were clarified:

* Design teams were aware of the phenomenon of a variable tax rate, due in large part to ADA participation rates in mainnet and unclaimed rewards  
* The original 5% rate with unclaimed rewards (variable tax rate) going to the treasury was expected to create a real tax rate of approximately 20%, but as the Shelley design specification was developed, further simulations were completed, indicating that this formula would create real tax rates in excess of 55%  
* The change to 20% with unclaimed rewards going to the reserve (where they would be distributed again, leading to what was being called “double taxation” in the post, something more accurately described as “additional variable rate”.  
* The expectation of this new formula would be a more consistent *tau* (*τ)*  rate of taxation, with less monetary emission going to the treasury.  Their simulations suggested a rate between 30% to 35% ([recent research](#cardano-economic-parameters) supports the accuracy, with consistent rates around 33%)

It is worth noting that in that discussion, there was positive reception by the design team for a reformulation where *tau* (*τ)* was applied only to **paid** rewards, rather than the whole reward pot.  This would result in a more transparent mechanism (though actual rates are unclear), however this was not investigated further, to our knowledge.

The discussion in the forum post led to the submission of a [CIP proposal](#pcp-forum-post) to further investigate the changing of the  *tau* (*τ)* parameter.  CIP editors moved the discussion to research, however the writer of the CIP decided to close the pull request based on low community engagement and feedback.

In October of 2023, a [PCP](#adjusting-the-rate-of-tau-\(t\)-\(pcp_treasurytax-tau-parameter_earncoinpool\)) (Parameter Change Proposal) for *tau* (*τ)* was introduced on the [Cardano Forum](#pcp-forum-post), and subsequently submitted for consideration by the Protocol Parameter Committee.  During the 5 months that the PCP was active, it was not pulled up to the main tri-weekly agenda of the Committee.  As of the March 2024 Committee meeting, there was no continuing effort from the community to refresh the PCP.  Of note for this PCP, was that solutions under consideration included setting the  *tau* (*τ)* rate as low as 0.03 in order to obtain a real rate closer to 5%, along with critical questions about factors that interacted with  *tau* (*τ)* and investigating the frequency of adjusting  *tau* (*τ).*  What was not included was any consideration of adjusting the target of  *tau* (*τ)* from the reward pot to the paid subset of the reward pot.  It is not clear that this is an infeasible approach, and should probably be discussed more broadly.

It is worth asking ourselves why these attempts to change the parameter were unsuccessful.  We would surmise, with some evidence, that (1) community engagement channels are not particularly strong for technical and economic parameters, and (2) that our ability to envision, as a community and as designers of protocol parameters, a clear model of how these complex parameters interact with each other and with exogenous factors such as cost to operate a node, regional exchange rates, etc., is not well supported yet.  We will touch on these challenges in the next section.

## 2.3 Understanding *tau* (*τ)* and other Parameters {#2.3-understanding-tau-(τ)-and-other-parameters}

The historical interrogation of *tau* (*τ)* highlights for us a critical aspect of not only *tau* (*τ)* but of all of our parameters, which is that they describe a complex topography of many factors, all interacting in unexpected ways.  We believe that in order to make good decisions regarding parameters in the future, we must work from robust, open source models and the data they create.  There is excellent work being done in the ecosystem, including data visibility (research and discussion around data dashboards), [open source calculation models](#cf-java-rewards-calculation) and deep dives into protocol parameter interactions ([this report](#cardano-economic-parameters) from Massimo Morini et al is both timely and timeless).  In both cases, discussion of real parameter modeling is either implicit, or listed explicitly as a need of the ecosystem, and we couldn’t agree more.

To that end, we include here an evaluative framework for what constitutes a “robust” model or approach to modeling.  This is relevant to this governance action in two ways:

* Short term, we can ask “Does this governance proposal support, imply or use any of these concepts?”  
* Long term, as models are created and iterated, it gives us a framework for assessing whether they are adequate, robust and effective over time, by allowing us to assess the models for gaps or oversights when suggesting parameter changes

### 2.3.1 Basic Evaluation Framework for modeling Parameters {#2.3.1-basic-evaluation-framework-for-modeling-parameters}

Models are like thought experiments, but with code. Something in between a proposed specification and a final implementation. This is great if you want to test an idea before building it, or want to test variations on an idea to see which might be best.

When creating a model, the point is to help you explore an idea, but also to help others do the same. As such, we must look for the following features and concepts:

##### **Legibility**

A model is a living document. It conveys information, but you can also modify and interact with it to learn new information. The results of running a model are only a small part of its value. Most of the value comes from people's ability to explore and modify the parameters and assumptions within the model to better understand something. This requires your model to be legible. Code syntax and guidance on best practices are areas to evolve and improve in this area.

* Is your model structured so that it's easy to interact with?  
* Could people easily modify it to test your assumptions and their own?


##### **Assumptions**

Models make assumptions about the world in order to focus on the thing that is being modeled. The model is a representation of a thing, not the thing itself. Just like with a map, it's important to specify what you included, what you left out, and why. It's also important to specify what you're assuming to be true and/or external states/environments that you assume the model is operating within.

* What does your model assume or require to be true?  
* Are these assumptions stated explicitly?


##### **Ergodicity**

[Visit all parts of the space that the system moves in](https://en.wikipedia.org/wiki/Ergodicity), in a uniform and random sense. A sufficiently large collection of random samples from a process can represent the average statistical properties of the entire process. Then you understand the full range of the state space and what states are more likely with what parameters.

##### **Specificity**

Specificity is the opposite of assumptions. It's what the model is exploring in detail.

* What question is the model exploring?  
* What did you choose to be specific about in relation to this question?  
* Is your model specific enough that it defines the problem and the potential solution?

##### **A/B Testing**

A/B testing allows you to test multiple variations of a thing. This is very important if you need to see how a proposed solution might behave under a wide range of assumptions. Be aware that A then B is not the same as testing A and B simultaneously. Statefulness and ordering is important. The latter compares A and B against the same data and this is what we're talking about when we say A/B testing.

* Test the same idea under multiple contexts.  
* Test multiple ideas within the same context.

##### **Data Generation**

Models also allow you to generate new data. This can be useful if you want to test alternate scenarios and explore the state space more than what would be possible with historical data.  
If your assumptions are made explicit then you can also test your model in different contexts. That way you can have a better idea of under what macro conditions your assumptions might hold.

##### **Reflexivity**

Reflexivity happens when multiple variables within the model feed into each other. This can create exponential amplification or suppression of metrics. This throws off wild data that makes it difficult to gain any understanding from the model. If there's any reflexivity involved make sure it's there for a very good reason and you understand exactly how it works.

* Are there any portions of your model that are self referential or that refer to each other in a loop?

## 2.4 Proposal Evaluation {#2.4-proposal-evaluation}

We will first examine some formal qualities of the proposal, and then move on to interrogating the proposal for specific fundamental principles.

##### **Formal qualities**

We are asking first how well the facts of the proposal reflect our own understanding and investigation of the facts.

Our first conclusion is that this proposal consistently misrepresents certain elements.  It repeatedly refers to *tau* (*τ)* as being set “arbitrarily” during Shelley genesis, however our investigation indicates that not only was it set in a methodical way, but that it was quite deliberately set in a systematic way as well, with ongoing simulation and analysis resulting in a very close approximation of the expected “real tax rate” (33%).  Further, the proposal suggests that *tau* (*τ)* has never been reassessed.  Again our investigation disputes this, as *tau* (*τ)* was undergoing a process of reassessment even as it was being implemented, and then was revisited twice with community driven discussions, CIP proposals and PCP requests.  We would agree that the parameter has not been given *enough* attention, and that this addition to the discussion is warranted.

Also in regards to the presentation of facts and context, Plutus V3 is raised in an odd way.  For clarity, this section could be removed, as the only overlap to be taken into consideration is that “parameters can be changed.”  We believe there is adequate awareness of this context, and that introducing the concept of PlutusV3 adds an inauthentic “name-dropping” quality to the presentation of the idea.  PlutusV3 is a legitimate and successful change adaptation to the protocol, but has almost no relevance to the idea being suggested here.  Conflating the PlutusV3 scoping (referred to as “structured approach” in the proposal) also misrepresents the vast difference between this proposal and that process.  There is a somewhat structured approach to this proposal, but nowhere near the technical and developmental [scoping that went into PlutusV3](#plutus-v3-on-testnet) and its long implementation.

The included mathematical representations are also not entirely accurate, reflecting direct correspondence of *tau* (*τ)* to real tax rate, but as we have seen there are complex interactions that drive real rates beyond the basic calculations of *tau* (*τ).*  A very useful resource that can currently be used to calculate this basic real rate, is the open source calculator and its [reports](#/report-latest/treasury_calculation) referenced earlier, and [explained here](#releasing-an-open-source-rewards-calculation).

We also ask what evidence supports claims being made in the proposal.  In particular there are numerous claims about future states of the incentives mechanism, but there also claims made about fiscal governance as well.  

There are some calculations that we believe do a decent job of describing two ways of viewing a principle that they repeat, namely that *price appreciation is the main driver of treasury sustainability*.  However, this is an area where A/B analysis described above is critical.  There is no evidence provided for why this principle might be true versus another principle like “*transaction growth drives treasury sustainability”* or even “*treasury spend security drives treasury sustainability”.*  Modeling these different contexts against similar data assumptions would provide evidence of pros and cons for each approach, and would likely indicate a navigable path if they proved to be polarities of each other (i.e. choice limiters akin to the blockchain trilemma).  In its current presentation, we do not find the claim of priority for a price appreciation approach, to the exclusion of other considerations, to be compelling.

##### **Principles guiding implementation**

We do find that any approach prioritizing security via the incentives mechanism would be welcome, however even then we would like to see more supporting evidence for how this parameter change leads to that.  The assumptions about more attractive stake participation driving security are non-obvious, in the sense that there are likely tradeoffs to be considered with the resource scarcity paradigm described, and how attractive use of the network will be for future stakeholders.  We are revisited here by the ad-hoc prioritization of price appreciation over usefulness or process, with no clear way to see the effects accumulating in each area.

Regarding the resource scarcity paradigm, the proposal describes one view of this where treasury distributions are governed more effectively and efficiently.  However no evidence or research is supplied to back this claim.  Resource scarcity *may* drive innovation and efficiency, but it may also exacerbate competition over collaboration.  When it comes to Cardano public goods, such extant political conflict is expected to be managed by constitutionally derived institutions that channel conflict in productive ways.  Cardano has only begun to develop such institutions, and in our opinion has a ways to go before we can dependably navigate difficult political questions without doing damage.  The proposers are encouraged to investigate this resource scarcity dynamic and to present both the pros and cons.  Modeling these factors would also present a better decision making environment for economic parameters.

The section of the proposal that discusses “continuity and prevention of disruptions” also needs to be developed more.  On the one hand it appears to be addressing the constitutionality of the governance action, which, while it may be a useful lens, does not seem to make sense in the overall structure of the proposal.  Giving constitutional alignment its own space makes sense, and clears this space for what may be the most important part of this proposal, given that we only have nascent capacity for real economic modeling:  monitoring and evaluation.

In complex environments, even with modeling to aid our decision-making, a robust approach to monitoring and evaluation (M\&E) is a must.  While it is appreciated that the proposers have highlighted some need for this, it is not acceptable that such mechanisms have not at least been given a framework.  An investigation into what existing institutions have the capacity to conduct such M\&E (protocol parameter committee in Intersect?  Independent community oversight institutions?) as well as the resources needed for such oversight is needed here.  A clear description of M\&E capacity is a requirement for ethical parameter change process, and that should be included for voters here.  

Finally, in accordance with the principle of “do no harm”, we would like to see such complex parameter changes undertaken with an eye toward *continuous development* and *iterative change*.  In the absence of robust modeling, and during an era where we want to develop such modeling capacity without cutting corners due to urgency, adopting small, iterative changes with effective M\&E procedures and clear pathways for reversibility is a critical development path.  For this proposal, the change from 20% to 10% can be characterized as not only a large change, but the maximum size change possible.  This type of pendulous approach to change is a disservice to stakeholders in the ecosystem who may not have, or understand, their immediate connections to a parameter like *tau* (*τ).*  

This asymmetry of stakeholder effects highlights an area of improvement for this proposal, which would be to widen the aperture of scoping, and try to include more voices that represent different roles. There is a strong bias towards SPOs/stakers, but much less consideration from the POV of developers or future stakeholders, for whom the treasury is the more significant public good.  Nowhere is this highlighted more than in the assumption throughout that there is one primary to be considered, *price appreciation*.  When added to the resource scarcity paradigm that is presented as an opportunity, we believe it creates a large risk of short term thinking at a time when decisions need to be made about long term roadmaps and product discussions for Cardano.

# 3.0 Conclusion {#3.0-conclusion}

Ultimately, we find that the proposal is not widely representative of stakeholders in the ecosystem, does not provide enough evidence for the claims of sustainability and benefit that is expected to accrue to all stakeholders, and does not take a careful approach to navigating complex change.

Having said that, it is the belief of this DRep that the most important discussions we can be having in Cardano governance right now relate to *Cardano Citizen Rights,* and evolving the Constitution over the short and intermediate term to enshrine those rights.  To that end, any discussions around monetary policy, and especially parameters related to the “taxes” being levied under this protocol are critical.

In other words, anything even tangentially related to the “tax rates” of Cardano are likely to inform our understanding of our constitutional protections in this ecosystem.  So we are deeply appreciative, and not at all surprised, that  *tau* (*τ)* has made an early appearance in our governance processes, and we look forward to evolving the discussion and ultimately the understanding around this key parameter.

To that end, there are several suggestions that can be made to bring us closer to a state where  *tau* (*τ)* changes in dynamical and useful ways, securing to us the most legitimate form of our constitutional rights:

* Include as complete of a history as possible for this or any parameter that we seek to change  
* Prioritize the development of our capacity to model complex parameters alongside exogenous data and scenarios  
* Prioritize the development of our capacity for monitoring and evaluation of change and attempted change in the ecosystem  
* When uncertainty to complexity prevent us from seeing more than one change request into our features, adopt a stance of continuous improvement and iterative change  
* Always provide a description of how and under what circumstances a reversal of the proposed policy, if implemented, would be prudent  

I look forward to the evolution of this parameter proposal, and to enjoying a legitimate *tau* (*τ)* parameter that adapts to and serves the ecosystem at its highest potential.

DRep ID:  drep1y239dn6nzlrlua9ku2d0jr4j3l6f344shcmjljtpt9mu6ps4u76rw  
DRep Profile (tempo): [https://tempo.vote/drep-profile?dRepId=drep1y239dn6nzlrlua9ku2d0jr4j3l6f344shcmjljtpt9mu6ps4u76rw](https://tempo.vote/drep-profile?dRepId=drep1y239dn6nzlrlua9ku2d0jr4j3l6f344shcmjljtpt9mu6ps4u76rw)

Stay in touch\!  
ReachYourPeople: [https://www.ryp.io/projects/45](https://www.ryp.io/projects/45)  
X:  [https://x.com/styg50](https://x.com/styg50)

## 4.0 References/Sources {#4.0-references/sources}

* ### [Iterating for growth with IOHK research](https://iohk.io/en/blog/posts/2020/06/25/iterating-for-growth-with-iohk/) {#iterating-for-growth-with-iohk-research}

* ### [Engineering Design Specification for Delegation and Incentives in Cardano–Shelley](https://github.com/input-output-hk/cardano-ledger/releases/latest/download/shelley-delegation.pdf)

* ### [CIP-1694](https://www.1694.io/en)

* ### [Double treasury taxation of 40% and possible workarounds](https://forum.cardano.org/t/double-treasury-taxation-of-40-and-possible-workarounds/41461) {#double-treasury-taxation-of-40%-and-possible-workarounds}

* ### [Cardano Economic Parameters](https://ucarecdn.com/cb24f376-d3bd-40c3-9c29-04573a644c8a/) {#cardano-economic-parameters}

* ### [CIP-Treasury fraction on actual distributed rewards](https://github.com/cardano-foundation/CIPs/pull/35)

* ### [Adjusting the Rate of Tau (t)](https://docs.google.com/document/d/1j7tE7GOD6W89A2SDJS0w3mS5s767zL8AyZIj5jPkuJo/edit?tab=t.0#heading=h.20o60lwg9tyl)   [(PCP\_TreasuryTax-tau-parameter\_EarnCoinPool)](https://docs.google.com/document/d/1j7tE7GOD6W89A2SDJS0w3mS5s767zL8AyZIj5jPkuJo/edit?tab=t.0#heading=h.20o60lwg9tyl) {#adjusting-the-rate-of-tau-(t)-(pcp_treasurytax-tau-parameter_earncoinpool)}

* ### [PCP Forum Post](https://forum.cardano.org/t/pcp-treasurytax-tau-parameter-earncoinpool/123245) {#pcp-forum-post}

* ### [cf-java-rewards-calculation](https://github.com/cardano-foundation/cf-java-rewards-calculation) {#cf-java-rewards-calculation}

* ### [Releasing an open source rewards calculation](https://www.cardanofoundation.org/blog/releasing-an-open-source-rewards-calculation) {#releasing-an-open-source-rewards-calculation}

* ### [/report-latest/treasury\_calculation](https://cardano-foundation.github.io/cf-java-rewards-calculation/report-latest/treasury_calculation.html) {#/report-latest/treasury_calculation}

* ### [Plutus V3 on TestNet](https://medium.com/tap-in-with-taptools/plutus-v3-on-testnet-5130d1e4838a) {#plutus-v3-on-testnet}

  ### 

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAQAQMAAAAs1s1YAAAABlBMVEUAAABER0byc6G0AAAAAXRSTlMAQObYZgAAAB9JREFUeF5jYEAD9h8YmEA0MwOYZmSWWQjhs4H56BgAT4ECDeGaeV4AAAAASUVORK5CYII=>