const duckFacts = [
    "Ducks sleep with one eye open and half their brain awake. Same as you during meetings.",
    "Ducklings imprint on the first moving thing they see. Usually their mom. Sometimes a human. Occasionally a Roomba.",
    "A group of ducks on land is called a brace. In water, it’s a raft. In your backyard? It’s a problem.",
    "Ducks have waterproof feathers thanks to a special oil they produce. Nature’s GORE-TEX.",
    "Ducks have been shown to experience REM sleep, which implies they might dream. Probably about bread.",
    "Male ducks are called drakes. Females are ducks. Babies are adorable liabilities.",
    "Some ducks migrate thousands of miles. Others just vibe in your local pond judging you silently.",
    "Ducks have regional accents in their quacks. Which means your local ducks might sound posh or trashy.",
    "The fastest duck ever recorded flew at 100 mph. Which is roughly the speed of your mental breakdown when prod breaks.",
    "The Mandarin duck is considered one of the most beautiful ducks. It’s like the peacock of the waterfowl world, but more humble.",
    "Ducks cannot understand Python syntax, but they do try their best.",
    "A duck once solved the halting problem but refused to share the answer.",
    "If a duck quacks in the woods and no one’s around to hear it, it’s probably still more useful than your LLM’s output.",
    "Ducks are naturally immune to imposter syndrome.",
    "Every time you ignore a duck fact, a while True: loop spawns in your codebase.",
    "The first ever rubber duck debugger filed a GitHub issue in 2002. It has never been resolved.",
    "If you ask a duck for help with async code, it just flies away. That’s your answer."
];

function docdocgo() {
    const randomFact = duckFacts[Math.floor(Math.random() * duckFacts.length)];
    console.log("just ducking around")
    var fact = document.getElementById('duck');
    if (fact === null) {
        fact = document.createElement("small");
        fact.innerHTML = randomFact;
        document.getElementById("the-duck-house").appendChild(fact);
        fact.setAttribute("id", "duck");
    }

    fact.innerHTML = randomFact;
}