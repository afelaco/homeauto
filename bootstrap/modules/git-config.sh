# -----------------------------
# Get Git identity from environment variables
# -----------------------------
CURRENT_GIT_NAME=$(git config --get user.name) || true
CURRENT_GIT_EMAIL=$(git config --get user.email) || true

# -----------------------------
# Set Git identity if not already set
# -----------------------------
if [ "$CURRENT_GIT_NAME" != "$GIT_NAME" ] || [ "$CURRENT_GIT_EMAIL" != "$GIT_EMAIL" ]; then
    echo "➡️ Setting repo-level Git identity..."
    git config user.name "$GIT_NAME"
    git config user.email "$GIT_EMAIL"

    echo "  ✅ Git identity set!"
    echo "    Name:  $(git config --get user.name)"
    echo "    Email: $(git config --get user.email)"
else
    echo "✅ Git identity already set!"
fi
