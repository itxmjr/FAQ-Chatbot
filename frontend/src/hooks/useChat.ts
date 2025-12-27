"use client";

import { useState, useCallback } from 'react';

export interface Message {
    id: string;
    type: 'user' | 'bot';
    content: string;
    timestamp: Date;
    matchedQuestion?: string;
    confidenceScore?: number;
}

interface ApiResponse {
    answer: string;
    matched_question: string | null;
    confidence_score: number;
}

const API_BASE_URL = "/api";

async function fetchBotResponse(question: string): Promise<ApiResponse> {
    const response = await fetch(`${API_BASE_URL}/ask`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
    });

    if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
    }

    return response.json();
}

export function useChat() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [isThinking, setIsThinking] = useState(false);

    const sendMessage = useCallback(async (content: string) => {
        if (!content.trim()) return;

        const userMessage: Message = {
            id: `user-${Date.now()}`,
            type: 'user',
            content: content.trim(),
            timestamp: new Date(),
        };

        setMessages(prev => [...prev, userMessage]);
        setIsThinking(true);

        try {
            const response = await fetchBotResponse(content.trim());

            const botMessage: Message = {
                id: `bot-${Date.now()}`,
                type: 'bot',
                content: response.answer,
                timestamp: new Date(),
                matchedQuestion: response.matched_question || undefined,
                confidenceScore: response.confidence_score,
            };

            setMessages(prev => [...prev, botMessage]);
        } catch (error) {
            console.error('Failed to fetch response:', error);

            const errorMessage: Message = {
                id: `bot-${Date.now()}`,
                type: 'bot',
                content: 'Sorry, I encountered an error while processing your request. Please make sure the backend server is running and try again.',
                timestamp: new Date(),
                confidenceScore: 0,
            };

            setMessages(prev => [...prev, errorMessage]);
        } finally {
            setIsThinking(false);
        }
    }, []);

    const clearMessages = useCallback(() => {
        setMessages([]);
    }, []);

    return {
        messages,
        isThinking,
        sendMessage,
        clearMessages,
    };
}
