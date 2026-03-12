import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function MindBloomWelcome() {
  const [theme, setTheme] = useState("neutral");
  const [showSecond, setShowSecond] = useState(false);

  // Theme color mapping
  const themes = {
    neutral: {
      bg: "bg-gradient-to-b from-white to-green-50",
      text: "text-gray-800",
    },
    ReadEasy: {
      bg: "bg-gradient-to-b from-blue-50 to-blue-100",
      text: "text-blue-800",
    },
    Focus: {
      bg: "bg-gradient-to-b from-green-50 to-green-100",
      text: "text-green-800",
    },
    ListenSee: {
      bg: "bg-gradient-to-b from-coral-50 to-orange-100",
      text: "text-orange-800",
    },
    Balanced: {
      bg: "bg-gradient-to-b from-purple-50 to-pink-50",
      text: "text-purple-800",
    },
  };

  const modes = [
    {
      name: "ReadEasy",
      icon: "🌿",
      title: "ReadEasy Style",
      description: "Clear, calm, and simple — words made friendly.",
    },
    {
      name: "Focus",
      icon: "⚡",
      title: "Focus Style",
      description: "Simple, calm, and distraction-free — your space to zone in.",
    },
    {
      name: "ListenSee",
      icon: "🎧",
      title: "Listen & See Style",
      description: "Hear it. Read it. See it — your way.",
    },
    {
      name: "Balanced",
      icon: "🌸",
      title: "Balanced Style",
      description: "A little of everything, made just right.",
    },
  ];

  return (
    <div className={`min-h-screen flex flex-col items-center justify-center transition-all duration-700 ${themes[theme].bg} ${themes[theme].text}`}>
      <AnimatePresence>
        {!showSecond && (
          <motion.div
            key="first"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 2 }}
            className="flex flex-col items-center justify-center"
          >
            <motion.h1
              style={{ fontFamily: 'Comic Sans MS, cursive, sans-serif' }}
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 1.5 }}
              className="text-4xl md:text-6xl font-semibold text-center"
            >
              🌼 Welcome to MindBloom
            </motion.h1>
            <motion.p
              style={{ fontFamily: 'Comic Sans MS, cursive, sans-serif' }}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 1.5, duration: 1.5 }}
              className="mt-4 text-xl md:text-2xl text-center"
            >
              learning that grows with you 🌿
            </motion.p>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 3, duration: 1 }}
            >
              <button
                onClick={() => setShowSecond(true)}
                className="mt-10 px-8 py-3 bg-green-600 text-white rounded-full text-lg shadow-md hover:bg-green-700 transition"
              >
                Get Started →
              </button>
            </motion.div>
          </motion.div>
        )}

        {showSecond && (
          <motion.div
            key="second"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1 }}
            className="w-full flex flex-col divide-y divide-gray-200"
          >
            {modes.map((mode) => (
              <motion.div
                key={mode.name}
                className="flex flex-col items-center justify-center py-12 cursor-pointer h-1/4"
                onMouseEnter={() => setTheme(mode.name)}
                onMouseLeave={() => setTheme("neutral")}
                whileHover={{ scale: 1.02 }}
                transition={{ duration: 0.5 }}
              >
                <h2 style={{ fontFamily: 'Comic Sans MS, cursive, sans-serif' }} className="text-3xl font-bold mb-2">{mode.icon} {mode.title}</h2>
                <p className="text-lg opacity-90">{mode.description}</p>
                {theme === mode.name && (
                  <motion.div
                    className="mt-4 text-center text-base italic opacity-80"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.6 }}
                  >
                    {mode.name === "ReadEasy" && (
                      <>
                        <p className="animate-pulse">Softly highlighted lines appear...</p>
                        <span className="text-2xl">🎧</span>
                      </>
                    )}
                    {mode.name === "Focus" && (
                      <>
                        <p>Calm green tone with gentle focus dots 🌱</p>
                      </>
                    )}
                    {mode.name === "ListenSee" && (
                      <>
                        <p>Speech bubbles and captions appear ☁️</p>
                      </>
                    )}
                    {mode.name === "Balanced" && (
                      <>
                        <p>Balanced bloom animation 🌸</p>
                      </>
                    )}
                  </motion.div>
                )}
              </motion.div>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
