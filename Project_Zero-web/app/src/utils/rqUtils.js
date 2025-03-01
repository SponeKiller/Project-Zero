export const toSnakeCase = (data) => {
    // Transforming indexes from camelCase to snake_case
    if (Array.isArray(data)) {
      return data.map(toSnakeCase);
    } else if (typeof data === "object" && data !== null) {
      return Object.fromEntries(
        Object.entries(data).map(([key, value]) => [
          key.replace(/([A-Z])/g, "_$1").toLowerCase(),
          toSnakeCase(value),
        ])
      );
    }
    return data;
  };
  