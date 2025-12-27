"use client";

import { useState, useRef, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Send, Sparkles, Command } from 'lucide-react';

interface CommandBarProps {
  onSend: (message: string) => void;
  isThinking: boolean;
  prefillValue?: string;
  onPrefillConsumed?: () => void;
}

export function CommandBar({ onSend, isThinking, prefillValue, onPrefillConsumed }: CommandBarProps) {
  const [input, setInput] = useState('');
  const [isFocused, setIsFocused] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (prefillValue && prefillValue !== input) {
      setInput(prefillValue);
      inputRef.current?.focus();
      onPrefillConsumed?.();
    }
  }, [prefillValue, onPrefillConsumed]);

  const hasInput = input.trim().length > 0;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (hasInput && !isThinking) {
      onSend(input);
      setInput('');
    }
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        inputRef.current?.focus();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="fixed bottom-4 md:bottom-6 left-1/2 -translate-x-1/2 w-full max-w-lg md:max-w-xl px-4 md:px-6 z-40">
      <motion.form
        onSubmit={handleSubmit}
        initial={{ opacity: 0, y: 30, scale: 0.95 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: 0.6, ease: [0.4, 0, 0.2, 1], delay: 0.3 }}
        className={`
          glass-premium rounded-2xl transition-all duration-500 ease-premium
          ${isFocused ? 'glow-gold ring-1 ring-gold/30' : ''}
          ${hasInput && !isThinking ? 'glow-gold-soft' : ''}
        `}
      >
        <div className="flex items-center gap-3 md:gap-4 px-4 py-3 md:py-3.5">
          <motion.div
            animate={isThinking ? {
              rotate: [0, 360],
              scale: [1, 1.1, 1]
            } : {}}
            transition={isThinking ? {
              rotate: { duration: 2, repeat: Infinity, ease: 'linear' },
              scale: { duration: 1, repeat: Infinity }
            } : {}}
            className={`flex-shrink-0 w-8 h-8 md:w-10 md:h-10 rounded-lg md:rounded-xl flex items-center justify-center transition-all duration-300 ${isThinking
              ? 'bg-gold/20'
              : isFocused
                ? 'bg-gold/10'
                : 'bg-surface-elevated'
              }`}
          >
            <Sparkles className={`w-4 h-4 md:w-5 md:h-5 transition-colors duration-300 ${isThinking || isFocused ? 'text-gold' : 'text-muted-foreground'
              }`} />
          </motion.div>

          {/* Input Field */}
          <input
            ref={inputRef}
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
            placeholder={isThinking ? "Processing your query..." : "Ask anything..."}
            disabled={isThinking}
            className="input-premium flex-1 text-base py-2"
          />

          <div className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-surface-elevated text-muted-foreground/50">
            <Command className="w-3 h-3" />
            <span className="text-xs font-medium">K</span>
          </div>

          <motion.button
            type="submit"
            disabled={!hasInput || isThinking}
            whileHover={hasInput && !isThinking ? { scale: 1.05 } : {}}
            whileTap={hasInput && !isThinking ? { scale: 0.95 } : {}}
            className={`
              flex-shrink-0 w-10 h-10 md:w-12 md:h-12 rounded-lg md:rounded-xl flex items-center justify-center
              transition-all duration-300 ease-premium
              ${hasInput && !isThinking
                ? 'bg-gradient-to-br from-gold to-gold-dim shadow-lg'
                : 'bg-surface-elevated cursor-not-allowed'
              }
            `}
          >
            <Send className={`w-4 h-4 md:w-5 md:h-5 ${hasInput && !isThinking ? 'text-background' : 'text-muted-foreground'}`} />
          </motion.button>
        </div>
      </motion.form>

      {/* Hint Text */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8 }}
        className="text-center text-xs text-muted-foreground/40 mt-4"
      >
        Press Enter to send • Powered by AI
      </motion.p>
    </div>
  );
}
